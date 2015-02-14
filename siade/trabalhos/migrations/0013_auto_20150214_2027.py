# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0012_auto_20150214_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciclo',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visita',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visita',
            name='pendencia',
            field=models.PositiveIntegerField(default=0, verbose_name='pend\xeancia', choices=[(0, 'Nenhuma'), (1, 'Fechada'), (2, 'Recusada')]),
            preserve_default=True,
        ),
    ]
