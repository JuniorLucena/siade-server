# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='municipio',
            field=models.ForeignKey(to='imoveis.Municipio', null=True),
            preserve_default=True,
        ),
    ]
