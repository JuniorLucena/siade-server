# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agentes', '0002_auto_20150302_2114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agente',
            options={'ordering': ('nome', 'sobrenome'), 'verbose_name': 'agente', 'verbose_name_plural': 'agentes'},
        ),
        migrations.AlterField(
            model_name='agente',
            name='tipo',
            field=models.PositiveIntegerField(default=1, choices=[(1, 'Agente de campo'), (2, 'Supervisor')]),
            preserve_default=True,
        ),
    ]
