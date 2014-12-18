from common import *
import os

SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']
ALLOWED_HOSTS = [os.environ['OPENSHIFT_APP_DNS']]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['OPENSHIFT_APP_NAME'],
        'USER': os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],
        'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],
        'HOST': os.environ['OPENSHIFT_MYSQL_DB_HOST'],
        'PORT': os.environ['OPENSHIFT_MYSQL_DB_PORT']
    }
}
STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static')
