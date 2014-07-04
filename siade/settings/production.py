"""
Django settings for SIADE (production).
"""
import dj_database_url
from .common import *

DATABASES['default'] =  dj_database_url.config()
ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECRET_KEY = get_env_setting('DJANGO_SECRET_KEY')
DEBUG = False
TEMPLATE_DEBUG = False