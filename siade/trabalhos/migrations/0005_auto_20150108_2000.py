# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0004_auto_20141224_1851'),
        ('trabalhos', '0004_auto_20140923_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabalho',
            name='quadras',
            field=models.ManyToManyField(related_name='trabalhos', to='imoveis.Quadra'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='trabalho',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='trabalho',
            name='quadra',
        ),
    ]
