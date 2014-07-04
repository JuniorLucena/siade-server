'''
WSGI config for siade project.

It exposes the WSGI callable as a module-level variable named ``application``.
'''

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'siade.settings.production')

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())