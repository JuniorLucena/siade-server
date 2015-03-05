# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0002_auto_20150222_1430'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trabalho',
            options={'ordering': ('agente', 'ciclo', 'quadra__bairro__nome', 'quadra__numero')},
        ),
        migrations.AlterModelOptions(
            name='visita',
            options={'ordering': ('data', 'hora', 'ciclo', 'agente', 'imovel'), 'verbose_name': 'visita', 'verbose_name_plural': 'visitas'},
        ),
        migrations.AlterField(
            model_name='ciclo',
            name='ano_base',
            field=models.PositiveIntegerField(default=2015),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='visita',
            unique_together=set([]),
        ),
    ]
