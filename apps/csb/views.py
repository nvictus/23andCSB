from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import simplejson
from django.conf import settings

from apps.api.views import requires_login

@requires_login
def profile(request, client):
    print request.session.keys()
    return render(request, 'csb/profile.html')