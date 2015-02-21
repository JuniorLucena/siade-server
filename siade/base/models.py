from django.db import models
from django_extensions.db.fields import UUIDField


class BaseModel(models.Model):
    id = UUIDField(primary_key=True)

    class Meta:
        abstract = True
