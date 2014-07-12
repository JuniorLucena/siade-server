"""
Django base settings for SIADE
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ROOT_URLCONF = 'siade.urls'
WSGI_APPLICATION = 'siade.wsgi.application'
ALLOWED_HOSTS = []
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dummy')
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Application definition
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	'django_extensions',
	'south',
	'xadmin',
	'crispy_forms',
	'provider',
	'provider.oauth2',
	'rest_framework',
	'siade.imoveis',
	'siade.trabalhos',
	'siade.api',
	'siade.relatorios',
)

# middleware definition
MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Recife'
USE_I18N = True
USE_L10N = True
USE_TZ = True
USE_THOUSAND_SEPARATOR = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

# Global template dirs
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

REST_FRAMEWORK = {
	'DEFAULT_FILTER_BACKENDS': (
		'rest_framework.filters.DjangoFilterBackend',
	),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.SessionAuthentication',
		'rest_framework.authentication.OAuth2Authentication',
	),
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.DjangoModelPermissions',
	),
	'PAGINATE_BY': 10,                 # Default to 10
	'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
	'MAX_PAGINATE_BY': 100             # Maximum limit allowed when using `?page_size=xxx`.
}