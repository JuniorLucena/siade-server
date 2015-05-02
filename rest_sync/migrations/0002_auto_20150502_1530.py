# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rest_sync', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syncstate',
            name='version',
            field=django_extensions.db.fields.ShortUUIDField(unique=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
