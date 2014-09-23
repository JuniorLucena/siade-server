# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0002_auto_20140911_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciclo',
            name='atividade',
            field=models.ForeignKey(related_name=b'ciclos', default=1, to='trabalhos.Atividade'),
            preserve_default=False,
        ),
    ]
