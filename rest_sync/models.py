from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_extensions.db.fields import ShortUUIDField
from shortuuid import uuid


class SyncState(models.Model):
    object_type = models.ForeignKey(ContentType)
    object_id = ShortUUIDField()
    object = GenericForeignKey('object_type', 'object_id')
    changed = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    version = ShortUUIDField()

    @classmethod
    def get_for_object(cls, obj):
        object_type = ContentType.objects.get_for_model(type(obj))
        ret, c = cls.objects.get_or_create(object_type=object_type,
                                           object_id=obj.id)
        return ret

    class Meta:
        unique_together = ("object_type", "object_id")


def sync_post_save(instance, **kwargs):
    state = SyncState.get_for_object(instance)
    state.version = uuid()
    state.save()


def sync_post_delete(instance, **kwargs):
    state = SyncState.get_for_object(instance)
    state.version = uuid()
    state.deleted = True
    state.save()
