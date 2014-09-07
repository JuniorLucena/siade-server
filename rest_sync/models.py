from random import getrandbits
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_extensions.db.fields import ShortUUIDField


class SyncState(models.Model):
    object_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('object_type', 'object_id')
    changed = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    version = models.PositiveIntegerField()

    def update(self, instance, delete=False):
        object_type = ContentType.objects.get_for_model(type(instance))
        try:
            change = self.objects.get_or_create(object_type=object_type,
                                                object_id=instance.id)
        except DoesNotExist:
            change = self.__class__(object_type=object_type,
                                    object_id=instance.id)
        change.deleted = delete
        change.revision = getrandbits(32)
        change.save()

    def post_save(self, instance, **kwargs):
        self.update(instance, False)

    def post_delete(self, instance, **kwargs):
        self.update(instance, True)

    class Meta:
        unique_together = ("object_type", "object_id")
