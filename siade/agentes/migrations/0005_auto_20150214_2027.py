# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agentes', '0004_agente_municipio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
    ]
