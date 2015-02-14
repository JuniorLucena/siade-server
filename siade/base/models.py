from django.db import models
from django_extensions.db.fields import ShortUUIDField


class BaseModel(models.Model):
    id = ShortUUIDField(primary_key=True)

    class Meta:
        abstract = True
