# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0003_auto_20150305_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='validado',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
    ]
