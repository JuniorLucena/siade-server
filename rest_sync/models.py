from random import getrandbits
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_extensions.db.fields import ShortUUIDField


def gen_sync_version_id():
    return getrandbits(31)


class SyncState(models.Model):
    object_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('object_type', 'object_id')
    changed = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    version = models.PositiveIntegerField(default=gen_sync_version_id)

    @classmethod
    def update(self, instance, delete=False):
        change = self.get_for_object(instance)
        change.deleted = delete
        change.save()

    @classmethod
    def post_save(self, instance, **kwargs):
        self.update(instance, False)

    @classmethod
    def post_delete(self, instance, **kwargs):
        self.update(instance, True)

    @classmethod
    def get_for_object(cls, obj):
        object_type = ContentType.objects.get_for_model(type(obj))
        ret, c = cls.objects.get_or_create(object_type=object_type,
                                           object_id=obj.id)
        return ret

    class Meta:
        unique_together = ("object_type", "object_id")
