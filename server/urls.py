from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('core.urls')),
    url(r'^auth/', include('apps.api.urls')),
    url(r'^csb/',  include('apps.csb.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
