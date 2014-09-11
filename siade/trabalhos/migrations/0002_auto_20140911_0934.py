# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalciclo',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalCiclo',
        ),
        migrations.RemoveField(
            model_name='historicaltrabalho',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalTrabalho',
        ),
        migrations.RemoveField(
            model_name='historicalvisita',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalVisita',
        ),
    ]
