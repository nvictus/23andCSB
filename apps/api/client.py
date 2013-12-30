import requests
import settings

# LIST OF SCOPES (The user must consent to each scope)
# --------------
# See https://api.23andme.com/docs/authentication/#scopes
# genomes
# basic
# names
# haplogroups
# ancestry
# relatives (write)
# analyses
# profile (read, write)
# publish
# introduction (read, write)
# rsXX or iXX
# phenotypes:read:<phenotype_id>
# phenotypes:write:<phenotype_id>
SCOPE = "basic names genomes analyses ancestry"

# leave these alone
BASE_URL = "https://api.23andme.com/1/"
LOGIN_URL = "https://api.23andme.com/authorize/?redirect_uri=%s&response_type=code&client_id=%s&scope=%s" % (settings.CALLBACK_URL, settings.CLIENT_ID, SCOPE)
OAUTH_KEY = "access_token"

class OAuthClient(object):
    def __init__(self, access_token=None):
        self.access_token = access_token

    def get_token(self, authorization_code):
        parameters = {
            'client_id': settings.CLIENT_ID,
            'client_secret': settings.CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': authorization_code, # the authorization code obtained above
            'redirect_uri': settings.CALLBACK_URL,
            'scope': SCOPE,
        }
        response = requests.post("https://api.23andme.com/token/", data=parameters)

        print "response.json: %s" % response.json()
        if response.status_code == 200:
            return (response.json()['access_token'], response.json()['refresh_token'])
        else:
            response.raise_for_status()

    def refresh_token(self, refresh_token):
        parameters = {
            'client_id': settings.CLIENT_ID,
            'client_secret': settings.CLIENT_SECRET,
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'redirect_uri': settings.CALLBACK_URL,
            'scope': SCOPE,
        }
        response = requests.post("https://api.23andme.com/token/", data=parameters)

        print "response.json: %s" % response.json()
        if response.status_code == 200:
            self.access_token = response.json()['access_token']
            return (response.json()['access_token'], response.json()['refresh_token'])
        else:
            response.raise_for_status()

    def _get_resource(self, resource):
        if self.access_token is None:
            raise Exception("access_token cannot be None")

        headers = {'Authorization': 'Bearer %s' % self.access_token}
        url = BASE_URL + resource
        response = requests.get(url, headers=headers, verify=False)

        #print "url: %s" % url
        #print "response: %s" % response

        if response.status_code == 200:
            #print "response.json: %s" % response.json()
            return response.text
        else:
            #print "Error [%d]" % response.status_code
            return response.text
            #response.raise_for_status()

    def _get_resource_demo(self, resource):
        if self.access_token is None:
            raise Exception("access_token cannot be None")

        headers = {'Authorization': 'Bearer %s' % self.access_token}

        url = BASE_URL + "demo/user/"
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            user = response.json()     
        else:
            response.raise_for_status()     
        profile_id = user['profiles'][0]['id']  

        if resource == 'names':
            url = BASE_URL + 'demo/names/'
        else:
            url = BASE_URL + 'demo/' + resource + '/' + profile_id
        response = requests.get(url, headers=headers, verify=False)

        #print "url: %s" % url
        #print "response: %s" % response

        if response.status_code == 200:
            #print "response.json: %s" % response.json()
            return response.text
        else:
            #print "Error [%d]" % response.status_code
            return response.text

    # USER
    # ====
    def get_user(self):
        if self.access_token is None:
            raise Exception("access_token cannot be None")
        headers = {'Authorization': 'Bearer %s' % self.access_token}
        url = BASE_URL + "user/"
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            return response.json()     
        else:
            response.raise_for_status()

    def get_names(self):
        return self._get_resource("names/")

    def get_profile_picture(self, profile_id):
        #GET, POST
        return self._get_resource("profile_picture/%s/" % profile_id)

    def get_publish(self, feature, profile_id, link_id=None):
        #GET, PUT, POST
        raise NotImplementedError

    def get_introduction(self, profile_id, match_id):
        #GET, PATCH, POST
        raise NotImplementedError


    # GENETICS
    # ========
    def get_genotype(self, profile_id, locations, unfiltered=False):
        # GET
        return self._get_resource("genotypes/?locations=%s" % locations)

    def get_phenotype(self, profile_id, phenotype_id):
        # GET, PUT
        raise NotImplementedError

    def get_all_snps(self, profile_id, unfiltered=False):
        return self._get_resource("genomes/%s/%s/?unfiltered=%s" % 
            (profile_id, feature, str(unfiltered).lower())
        )


    # ANCESTRY
    # ========
    def get_haplogroups(self, profile_id):
        raise NotImplementedError

    def get_ancestry(self, profile_id, threshold=0.75):
        #/ancestry/profile_id/?threshold=...
        raise NotImplementedError

    def get_neanderthal(self, profile_id):
        return self._get_resource("neanderthal/%s/" % profile_id)

    def get_relatives(self, profile_id, limit, offset, since, share_status, intro_status):
        #GET:  relatives/profile_id/?limit=x&offset=y&since=1348699925&share_status=z&intro_status=a
        #PATCH: relatives/profile_id/match_id/
        raise NotImplementedError

    # HEALTH
    # ======
    def get_risks(self, profile_id):
        return self._get_resource("risks/%s/" % profile_id)

    def get_carriers(self, profile_id):
        return self._get_resource("carriers/%s/" % profile_id)

    def get_drug_responses(self, profile_id):
        return self._get_resource("drug_responses/%s/" % profile_id)

    def get_traits(self, profile_id):
        return self._get_resource("traits/%s/" % profile_id)

