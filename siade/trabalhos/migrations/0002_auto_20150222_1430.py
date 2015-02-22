# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciclo',
            name='atividade',
            field=models.PositiveIntegerField(choices=[(1, 'Levantamento de \xcdndice (LI)'), (2, 'Tratamento (T)'), (3, 'Levantamento de \xcdndice + Tratamento (LI+T)')]),
            preserve_default=True,
        ),
    ]
