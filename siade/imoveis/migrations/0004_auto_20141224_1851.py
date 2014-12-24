# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0003_auto_20140923_0954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imovel',
            options={'ordering': ('ordem',), 'verbose_name': 'im\xf5vel', 'verbose_name_plural': 'im\xf3veis'},
        ),
        migrations.AlterUniqueTogether(
            name='imovel',
            unique_together=None,
        ),
    ]
