# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0008_auto_20150131_0133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trabalho',
            options={'ordering': ('agente', 'ciclo', 'quadra')},
        ),
        migrations.AlterUniqueTogether(
            name='trabalho',
            unique_together=set([('ciclo', 'quadra')]),
        ),
    ]
