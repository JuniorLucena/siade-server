# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.utils.translation import gettext as _
from django_extensions.db.fields import ShortUUIDField


class SyncModelMixin(models.Model):
    modificado = models.DateTimeField(
        auto_now=True, default=datetime.now, editable=False,
        verbose_name=_('modificado'))
    excluido = models.BooleanField(
        default=False, editable=False, verbose_name=_('excluído'))
    revisao = ShortUUIDField(auto=True)

    def save(self, *args, **kwargs):
        self.revisao = None
        return super(SyncModelMixin, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.excluido:
            return super(SyncModelMixin, self).delete(*args, **kwargs)
        else:
            self.excluido = True
            self.save()

    class Meta:
        abstract = True
