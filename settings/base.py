# Base settings for project
# -------------------------
import os
def get_env_setting(key, default=None):
    val = os.getenv(key, default)
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val

# Debugging
# =========
DEBUG = True
TEMPLATE_DEBUG = DEBUG
#DEBUG_PROPAGATE_EXCEPTIONS


# Routing
# =======
ROOT_URLCONF = 'server.urls'
WSGI_APPLICATION = 'server.wsgi.application'
ALLOWED_HOSTS = []


# Apps
# ====
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Useful template tags:
    # 'django.contrib.humanize',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'core',
)
# FIXTURE_DIRS

# Database
# ========
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
# DATABASE_ROUTERS
# DEFAULT_INDEX_TABLESPACE
# DEFAULT_TABLESPACE
# TRANSACTIONS_MANAGED


# Cache
# =====
# CACHES
# CACHE_MIDDLEWARE_ALIAS
# CACHE_MIDDLEWARE_ANONYMOUS_ONLY
# CACHE_MIDDLEWARE_KEY_PREFIX
# CACHE_MIDDLEWARE_SECONDS


# URLs
# ====
# ABSOLUTE_URL_OVERRIDES
# APPEND_SLASH
# PREPEND_WWW


# HTTP
# ====
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# DEFAULT_CHARSET
# DEFAULT_CONTENT_TYPE
# DISALLOWED_USER_AGENTS
# FORCE_SCRIPT_NAME
# INTERNAL_IPS
# SECURE_PROXY_SSL_HEADER
# SIGNING_BACKEND
# USE_ETAGS
# USE_X_FORWARDED_HOST


# Templates
# =========
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.static",
]
# TEMPLATE_STRING_IF_INVALID


# Static files
# ============
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = 'staticfiles'
# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
# STATICFILES_STORAGE


# File uploads
# ============
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''
# DEFAULT_FILE_STORAGE
# FILE_CHARSET
# FILE_UPLOAD_HANDLERS
# FILE_UPLOAD_MAX_MEMORY_SIZE
# FILE_UPLOAD_PERMISSIONS
# FILE_UPLOAD_TEMP_DIR


# Security
# ========
SECRET_KEY = ''
# CSRF_COOKIE_DOMAIN
# CSRF_COOKIE_NAME
# CSRF_COOKIE_PATH
# CSRF_COOKIE_SECURE
# CSRF_FAILURE_VIEW
# X_FRAME_OPTIONS


# Globalization (i18n/l10n)
# =========================
# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'


# Serialization
# =============
# DEFAULT_CHARSET
# SERIALIZATION_MODULES


# Error reporting
# ===============
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS
# SEND_BROKEN_LINK_EMAILS
# DEFAULT_EXCEPTION_REPORTER_FILTER
# IGNORABLE_404_URLS


# Email
# =====
# EMAIL_BACKEND
# EMAIL_FILE_PATH
# EMAIL_HOST
# EMAIL_HOST_PASSWORD
# EMAIL_HOST_USER
# EMAIL_PORT
# EMAIL_SUBJECT_PREFIX
# EMAIL_USE_TLS
# SERVER_EMAIL
# DEFAULT_CHARSET
# DEFAULT_FROM_EMAIL


# Logging
# =======
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# LOGGING_CONFIG


# Testing
# =======
# TEST_CHARSET
# TEST_COLLATION
# TEST_DEPENDENCIES
# TEST_MIRROR
# TEST_NAME
# TEST_CREATE
# TEST_USER
# TEST_USER_CREATE
# TEST_PASSWD
# TEST_TBLSPACE
# TEST_TBLSPACE_TMP
# TEST_RUNNER


# Other settings
# --------------

# Authentication
# ==============
# AUTHENTICATION_BACKENDS
# AUTH_USER_MODEL
# LOGIN_REDIRECT_URL
# LOGIN_URL
# LOGOUT_URL
# PASSWORD_RESET_TIMEOUT_DAYS
# PASSWORD_HASHERS

# Sessions
# ========
# SESSION_CACHE_ALIAS
# SESSION_COOKIE_AGE
# SESSION_COOKIE_DOMAIN
# SESSION_COOKIE_HTTPONLY
# SESSION_COOKIE_NAME
# SESSION_COOKIE_PATH
# SESSION_COOKIE_SECURE
# SESSION_ENGINE
# SESSION_EXPIRE_AT_BROWSER_CLOSE
# SESSION_FILE_PATH
# SESSION_SAVE_EVERY_REQUEST
# SESSION_SERIALIZER

# Comments
# ========
# COMMENTS_HIDE_REMOVED
# COMMENT_MAX_LENGTH
# COMMENTS_APP
# PROFANITIES_LIST

# Messages
# ========
# MESSAGE_LEVEL
# MESSAGE_STORAGE
# MESSAGE_TAGS

# Admindocs
# =========
# ADMIN_FOR

# Sites
# =====
SITE_ID = 1



