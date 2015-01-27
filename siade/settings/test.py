from common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('TEST_DB_NAME', 'siade'),
        'USER': os.environ.get('TEST_DB_USER', 'siade'),
        'PASSWORD': os.environ.get('TEST_DB_PASS', ''),
        'HOST': os.environ.get('TEST_DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('TEST_DB_PORT', 3306)
    }
}