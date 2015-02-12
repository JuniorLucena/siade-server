from django.db.models import signals
from .models import SyncState
from .views import ModelSyncView_factory

__version__ = '0.2.dev'


def sync_register(model, **kwargs):
    model.sync_state = True
    signals.post_save.connect(SyncState.post_save, sender=model,
                              weak=False)
    signals.post_delete.connect(SyncState.post_delete, sender=model,
                                weak=False)

def sync_unregister(model):
    del model.sync_state
    signals.post_save.disconnect(SyncState.post_save, sender=model)
    signals.post_delete.disconnect(SyncState.post_delete, sender=model)

