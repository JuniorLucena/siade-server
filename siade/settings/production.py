"""
Django settings for SIADE (production).
"""
import os
import dj_database_url
from .common import *

DATABASES['default'] =  dj_database_url.config()
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = list(INSTALLED_APPS) + ['gunicorn']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = False
TEMPLATE_DEBUG = False