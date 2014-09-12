# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='cpf',
            field=models.BigIntegerField(unique=True, verbose_name=b'CPF'),
        ),
    ]
