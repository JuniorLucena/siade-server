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

# debug toolbar
DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_PANELS = [
    #'debug_toolbar.panels.versions.VersionsPanel',
    #'debug_toolbar.panels.timer.TimerPanel',
    #'debug_toolbar.panels.settings.SettingsPanel',
    #'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    #'debug_toolbar.panels.sql.SQLPanel',
    #'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    #'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]