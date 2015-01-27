from common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['TEST_DB_NAME'],
        'USER': os.environ['TEST_DB_USER'],
        'PASSWORD': os.environ['TEST_DB_PASS'],
        'HOST': os.environ['TEST_DB_HOST'],
        'PORT': os.environ['TEST_DB_PORT']
    }
}