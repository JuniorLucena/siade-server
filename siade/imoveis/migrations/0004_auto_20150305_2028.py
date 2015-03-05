# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0003_auto_20150303_1943'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='imovel',
            unique_together=set([('numero', 'lado')]),
        ),
    ]
