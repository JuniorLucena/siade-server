# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0007_auto_20150131_0123'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='trabalho',
            unique_together=set([('ciclo', 'agente', 'quadra')]),
        ),
    ]
