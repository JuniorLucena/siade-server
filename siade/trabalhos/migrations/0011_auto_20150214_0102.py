# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import siade.trabalhos.models


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
            field=models.PositiveIntegerField(verbose_name=siade.trabalhos.models.Atividade, choices=[(1, 'Levantamento de \xcdndice (LI)'), (1, 'Tratamento (T)'), (1, 'Levantamento de \xcdndice + Tratamento (LI+T)')]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Atividade',
        ),
        migrations.AlterField(
            model_name='visita',
            name='pendencia',
            field=models.PositiveIntegerField(default='Nenhuma', verbose_name='pend\xeancia', choices=[('Nenhuma', 'Nenhuma'), (1, 'Fechada'), (2, 'Recusada')]),
            preserve_default=True,
        ),
    ]
