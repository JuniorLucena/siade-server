# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0002_auto_20140911_0934'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='imovel',
            unique_together=set([('lado', 'numero')]),
        ),
        migrations.AlterUniqueTogether(
            name='ladoquadra',
            unique_together=set([('quadra', 'numero')]),
        ),
        migrations.AlterUniqueTogether(
            name='quadra',
            unique_together=set([('bairro', 'numero')]),
        ),
    ]
