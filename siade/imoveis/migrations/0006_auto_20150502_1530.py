# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0005_auto_20150313_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='habitantes',
            field=models.PositiveIntegerField(default=0, verbose_name='qtd. habitantes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imovel',
            name='ordem',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
