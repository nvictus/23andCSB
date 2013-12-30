from .base import *

DEBUG = get_env_setting('DEBUG')
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = get_env_setting('SECRET_KEY')

### Dev database config
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
###

# 23andMe API
# TODO: Make these equal to what's in your dev dashboard at
# http://api.23andme.com/dev/
INSTALLED_APPS += (
    'apps.api',
    'apps.csb',
)
CLIENT_ID = get_env_setting('CLIENT_ID')
CLIENT_SECRET = get_env_setting('CLIENT_SECRET')
CALLBACK_URL = get_env_setting('CALLBACK_URL')



### Cache config
# # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     }
# }
###

### Debugging toolbar config
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
# INSTALLED_APPS += (
#     'debug_toolbar',
# )

# # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
# INTERNAL_IPS = ('127.0.0.1',)

# # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
# MIDDLEWARE_CLASSES += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# )

# # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
#     'SHOW_TEMPLATE_CONTEXT': True,
# }
###