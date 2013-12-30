from django.conf.urls import patterns, include, url

# NOTE: django loads templates automatically from apps in INSTALLED_APPS.
# Put a templates folder in your core application package and store 
# common templates and layouts in that template root.
# Don't bother adding anything to TEMPLATE_DIRS... I would very much prefer
# to avoid introducing any filesystem introspection in the settings file.
# It's almost as ugly and inelegant as messing with sys.path

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('core.urls')),
    url(r'^auth/', include('apps.api.urls')),
    url(r'^csb/',  include('apps.csb.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)

# TODO: automatically include in the urls of any submodule of apps
# i.e. url(r'^mycoolapp', include('apps.mycoolapp.urls'))
# Or maybe use settings to see which apps are currently loaded...

# TODO: add boilerplate to serve static files directly
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns()
# import settings
# urlpatterns += patterns('',
#     (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
# )