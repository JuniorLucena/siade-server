# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='qrcode',
            field=models.CharField(max_length=32, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
