# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0007_auto_20150204_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bairro',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imovel',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ladoquadra',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logradouro',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='municipio',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quadra',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uf',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
    ]
