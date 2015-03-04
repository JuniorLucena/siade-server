# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0002_imovel_qrcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bairro',
            options={'ordering': ('municipio', 'nome')},
        ),
        migrations.AlterModelOptions(
            name='uf',
            options={'ordering': ('nome',), 'verbose_name': 'estado'},
        ),
        migrations.AddField(
            model_name='quadra',
            name='sequencia',
            field=models.PositiveIntegerField(null=True, verbose_name='sequ\xeancia', blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='quadra',
            unique_together=set([('bairro', 'numero', 'sequencia')]),
        ),
    ]
