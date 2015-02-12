# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0009_auto_20150201_0952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trabalho',
            options={'ordering': ('agente', 'ciclo', 'quadra__id')},
        ),
        migrations.AddField(
            model_name='visita',
            name='imovel_inspecionado',
            field=models.NullBooleanField(verbose_name='im\xf3vel inspecionado'),
            preserve_default=True,
        ),
    ]
