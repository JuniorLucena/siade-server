from django.db.models import signals
from .models import SyncState
from .views import ModelSyncView_factory

__version__ = '0.1.dev'


class Synchonizer(object):

    def __init__(self):
        self._registry = {}

    def register(self, model, **kwargs):
        serializer_class = kwargs.get('serializer_class', None)
        queryset = kwargs.get('queryset', None)
        view_class = kwargs.get('view_class', None)

        if view_class is None:
            view_class = ModelSyncView_factory(model, serializer_class)
            if queryset is not None:
                view_class.queryset = queryset

        self._registry[model] = view_class

        signals.post_save.connect(SyncState.post_save, sender=model,
                                  weak=False)
        signals.post_delete.connect(SyncState.post_delete, sender=model,
                                    weak=False)

    def is_registered(model):
        return model in self._registry

    def unregister(self, model):
        del self._registry[model]
        signals.post_save.disconnect(SyncState.post_save, sender=model)
        signals.post_delete.disconnect(SyncState.post_delete, sender=model)

    def get_urls(self):
        from django.conf.urls import url, include
        urlpatterns = []
        for model, view_class in self._registry.items():
            urlpatterns += [
                url(r'^%s/%s/' % (model._meta.app_label,
                                  model._meta.model_name),
                    view_class.as_view()),
            ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), 'rest_sync', 'rest_sync'

synchonizer = Synchonizer()
urls = synchonizer.urls
