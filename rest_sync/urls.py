from django.conf.urls import patterns, url
from .views import SyncView, ListSyncModelsView

urlpatterns = patterns(
    '',
    url(r'^$', ListSyncModelsView.as_view()),
    url(r'^(?P<app>\w+)/(?P<model>\w+)/$', SyncView.as_view(),
        name='rest-synchro'),
)
