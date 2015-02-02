# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0003_ciclo_atividade'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='visita',
            unique_together=set([('ciclo', 'agente', 'imovel')]),
        ),
    ]
