# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0011_auto_20150214_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='pendencia',
            field=models.PositiveIntegerField(default=0, verbose_name='pend\xeancia', choices=[(0, 'Nenhuma'), (1, 'Fechada'), (2, 'Recusada')]),
            preserve_default=True,
        ),
    ]
