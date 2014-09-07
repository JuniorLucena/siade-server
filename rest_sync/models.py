from random import getrandbits
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_extensions.db.fields import ShortUUIDField


def gen_sync_version_id():
    return getrandbits(32)


class SyncState(models.Model):
    object_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('object_type', 'object_id')
    changed = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    version = models.PositiveIntegerField(default=gen_sync_version_id)

    def update(self, instance, delete=False):
        change = self.get_for_object(instance)
        change.deleted = delete
        change.save()

    def post_save(self, instance, **kwargs):
        self.update(instance, False)

    def post_delete(self, instance, **kwargs):
        self.update(instance, True)

    @staticmethod
    def get_for_object(obj):
        object_type = ContentType.objects.get_for_model(type(obj))
        ret, c = SyncState.objects.get_or_create(object_type=object_type,
                                                 object_id=obj.id)
        return ret

    class Meta:
        unique_together = ("object_type", "object_id")
