"""
Django settings for SIADE (development).
"""
from .common import *

DEBUG = True
TEMPLATE_DEBUG = True
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']
INSTALLED_APPS = list(INSTALLED_APPS) + ['debug_toolbar']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'siade.db'),
    }
}
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
CRISPY_FAIL_SILENTLY = False
