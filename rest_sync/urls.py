from django.conf.urls import patterns, url
from .views import SyncView

urlpatterns = patterns(
    '',
    url(r'^(?P<app>\w+)/(?P<model>\w+)$', SyncView.as_view(),
        name='rest-synchro'),
)
