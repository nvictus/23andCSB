from .base import *

DEBUG = get_env_setting('DEBUG', False)
TEMPLATE_DEBUG = DEBUG

########## SECRET CONFIGURATION
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION

########## HOST CONFIGURATION
ALLOWED_HOSTS = [get_env_setting('HOSTNAME')]
########## END HOST CONFIGURATION

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

########## DATABASE CONFIGURATION
import os
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
########## END DATABASE CONFIGURATION

########## CACHE CONFIGURATION
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     }
# }
########## END CACHE CONFIGURATION

########## EMAIL CONFIGURATION
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')
# EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')
# EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')
# EMAIL_PORT = environ.get('EMAIL_PORT', 587)
# EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
# EMAIL_USE_TLS = True
# SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION