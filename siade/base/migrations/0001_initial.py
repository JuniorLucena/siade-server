# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations
from django.core import management
from siade.agentes.management import create_or_update_groups


class Migration(migrations.Migration):

    dependencies = [
        ('agentes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_or_update_groups),
        migrations.RunPython(management.call_command('sitetree_resync_apps'))
    ]
