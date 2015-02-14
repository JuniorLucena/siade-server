# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0010_auto_20150212_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visita',
            name='atividade',
        ),
        migrations.AlterField(
            model_name='ciclo',
            name='atividade',
            field=models.PositiveIntegerField(choices=[(1, 'Levantamento de \xcdndice (LI)'), (1, 'Tratamento (T)'), (1, 'Levantamento de \xcdndice + Tratamento (LI+T)')]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Atividade',
        ),
    ]
