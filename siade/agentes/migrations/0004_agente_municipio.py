# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0004_auto_20141224_1851'),
        ('agentes', '0003_auto_20141224_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='agente',
            name='municipio',
            field=models.ForeignKey(blank=True, to='imoveis.Municipio', null=True),
            preserve_default=True,
        ),
    ]
