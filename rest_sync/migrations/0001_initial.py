# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyncState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', django_extensions.db.fields.ShortUUIDField(editable=False, blank=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('version', django_extensions.db.fields.ShortUUIDField(editable=False, blank=True)),
                ('object_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='syncstate',
            unique_together=set([('object_type', 'object_id')]),
        ),
    ]
