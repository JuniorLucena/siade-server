# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0013_auto_20150214_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='pendencia',
            field=models.PositiveIntegerField(default=1, verbose_name='pend\xeancia', choices=[(1, 'Nenhuma'), (2, 'Fechada'), (3, 'Recusada')]),
            preserve_default=True,
        ),
    ]
