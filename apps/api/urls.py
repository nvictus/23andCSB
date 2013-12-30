from django.conf.urls.defaults import patterns, url, include
from .views import callback, logout, get_resource

urlpatterns = patterns('', 
    url(r'^callback/$', callback),
    url(r'^logout/$', logout),
    url(r'^get_(?P<resource>.*)/$', get_resource),
)
