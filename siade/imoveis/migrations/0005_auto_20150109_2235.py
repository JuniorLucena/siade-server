# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0004_auto_20141224_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bairro',
            name='municipio',
            field=models.ForeignKey(related_name='bairros', on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Munic\xc3\xadpio', to='imoveis.Municipio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imovel',
            name='lado',
            field=models.ForeignKey(related_name='imoveis', on_delete=django.db.models.deletion.PROTECT, to='imoveis.LadoQuadra'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logradouro',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'munic\xc3\xadpio', blank=True, to='imoveis.Municipio', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quadra',
            name='bairro',
            field=models.ForeignKey(related_name='quadras', on_delete=django.db.models.deletion.PROTECT, to='imoveis.Bairro'),
            preserve_default=True,
        ),
    ]
