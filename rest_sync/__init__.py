from django.db.models import signals
from django.utils.functional import cached_property
from .models import SyncState, sync_post_save, sync_post_delete

__version__ = '0.2.dev'


def sync_register(model, **kwargs):
    model.sync_state = cached_property(lambda s: SyncState.get_for_object(s))
    signals.post_save.connect(sync_post_save, sender=model,
                              weak=False)
    signals.post_delete.connect(sync_post_delete, sender=model,
                                weak=False)
    return model


def sync_unregister(model):
    del model.sync_state
    signals.post_save.disconnect(SyncState.post_save, sender=model)
    signals.post_delete.disconnect(SyncState.post_delete, sender=model)
    return model
