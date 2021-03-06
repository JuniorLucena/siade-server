"""
Django base settings for SIADE
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

ROOT_URLCONF = 'siade.urls'
WSGI_APPLICATION = 'siade.wsgi.application'
ALLOWED_HOSTS = []
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dummy')
ADMINS = [(e.strip(), e.strip()) for e in os.environ.get('ADMINS_EMAILS', '').split(',')]


# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'input_mask',
    'activelink',
    'bootstrap3',
    'rest_framework',
    'qrcode',
    'rest_sync',
    'siade.base',
    'siade.agentes',
    'siade.imoveis',
    'siade.trabalhos',
    'siade.api',
    'siade.relatorios',
    'sitetree',
    'oauth2_provider',
    'django.contrib.admin',
    'bootstrap3_datetime',
    'djrill',
)

# middleware definition
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'siade.trabalhos.context_processors.ciclo_atual'
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Recife'
USE_I18N = True
USE_L10N = True
USE_TZ = False
USE_THOUSAND_SEPARATOR = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

# Global template dirs
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

BOOTSTRAP3 = {
    'required_css_class': 'required'
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissions',
    ),
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 100
}

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
AUTH_USER_MODEL = 'agentes.Agente'
APPEND_SLASH = True

# Email configuration
EMAIL_SUBJECT_PREFIX = '[SIADE] '
SERVER_EMAIL = os.environ.get('SERVER_EMAIL', 'webmaster@localhost')
DEFAULT_FROM_EMAIL = SERVER_EMAIL
MANDRILL_API_KEY = 'lwNLl0_-FNT5nOjT0orD1A'
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

# Logging configation
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
