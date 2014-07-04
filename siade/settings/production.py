"""
Django settings for SIADE (production).
"""
import dj_database_url
from .common import *

DATABASES['default'] =  dj_database_url.config()
ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECRET_KEY = '18(*)p%y$vq!_5bsq=nqi^-+63=wp@do55^(@yny8*d@9pv^bl'
DEBUG = False
TEMPLATE_DEBUG = False