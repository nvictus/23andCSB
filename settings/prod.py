from .base import *

DEBUG = get_env_setting('DEBUG', False)
TEMPLATE_DEBUG = DEBUG

########## SECRET CONFIGURATION
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION

########## HOST CONFIGURATION
ALLOWED_HOSTS = ['*']
########## END HOST CONFIGURATION

########## DATABASE CONFIGURATION
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
########## END DATABASE CONFIGURATION

########## CACHE CONFIGURATION
CACHES = {}
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