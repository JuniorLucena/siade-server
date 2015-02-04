# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0006_auto_20150131_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quadra',
            name='numero',
            field=models.PositiveIntegerField(default=0, verbose_name='n\xfamero'),
            preserve_default=True,
        ),
    ]
