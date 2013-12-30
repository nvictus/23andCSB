from django.http import HttpResponse
from django.shortcuts import redirect
import json

import logging
log = logging.getLogger("apidemo")

# import our OAuth client
from . import client

# view decorator
def requires_login(view_fcn):
    def wrapper(request, *args, **kwargs):
        if client.OAUTH_KEY in request.session.keys():
            c = client.OAuthClient(request.session[client.OAUTH_KEY])
            return view_fcn(request, c, *args, **kwargs)
        else:
            return redirect(client.LOGIN_URL)
    return wrapper


# views
def get_resource(request, resource):
    c = client.OAuthClient(request.session[client.OAUTH_KEY])

    if 'demo' in request.GET and request.GET['demo']=='true':
        return HttpResponse(c._get_resource_demo(resource))

    user = c.get_user()
    profile_id = user['profiles'][0]['id']

    if resource == 'names':
        data = c.get_names()
    elif resource == 'risks':
        data = c.get_risks(profile_id)
    elif resource == 'carriers':
        data = c.get_carriers(profile_id)
    elif resource == 'drug_responses':
        data = c.get_drug_responses(profile_id)
    elif resource == 'traits':
        data = c.get_traits(profile_id)
    elif resource == 'neanderthal':
        data = c.get_neanderthal(profile_id)
    else:
        raise Exception("invalid API resource requested")
    return HttpResponse(data, mimetype="application/json")

def callback(request):
    """ 
    The 23andMe api calls this view with a ?code=xxxxxx paramter.  This
    parameter is a short lived authorization code that you must use to get a an
    OAuth authorization token which you can use to retrieve user data.  This view
    uses database backed session to store the auth token instead of cookies in
    order to protect the token from leaving the server as it allows access to
    significant sensitive user information. 

    """
    # create a fresh client
    c = client.OAuthClient()

    # get code returned from 23andMe API after user login
    code = request.GET["code"]
    log.debug("code: %s" % code)

    # request token from 23andMe
    log.debug("fetching token...")
    (access_token, refresh_token) = c.get_token(code)
    log.debug("access_token: %s refresh_token: %s" % (access_token, refresh_token))

    log.debug("refreshing token...")
    (access_token, refresh_token) = c.refresh_token(refresh_token)
    log.debug("access_token: %s refresh_token: %s" % (access_token, refresh_token))

    # persist in the browser session database (not cookie)
    request.session[client.OAUTH_KEY] = access_token

    # authorize the API client
    c = client.OAuthClient(request.session[client.OAUTH_KEY])

    # store first and last name
    names_json = c.get_names()
    names = json.loads(names_json)
    request.session["name"] = "%s %s" % (names['first_name'], names['last_name'])

    return redirect("/csb/")

def logout(request):
    # clear browser session on logout
    log.debug("logging out...")
    request.session.clear()
    return redirect("/")
