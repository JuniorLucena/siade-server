# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalbairro',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalBairro',
        ),
        migrations.RemoveField(
            model_name='historicalimovel',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalImovel',
        ),
        migrations.RemoveField(
            model_name='historicalladoquadra',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalLadoQuadra',
        ),
        migrations.RemoveField(
            model_name='historicallogradouro',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalLogradouro',
        ),
        migrations.RemoveField(
            model_name='historicalquadra',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalQuadra',
        ),
        migrations.RemoveField(
            model_name='historicaltipoimovel',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalTipoImovel',
        ),
        migrations.AlterModelOptions(
            name='bairro',
            options={'ordering': ('municipio',)},
        ),
        migrations.AlterModelOptions(
            name='logradouro',
            options={'ordering': ('nome',)},
        ),
        migrations.AlterModelOptions(
            name='municipio',
            options={'verbose_name': 'munic\xedpio'},
        ),
        migrations.AlterModelOptions(
            name='uf',
            options={'verbose_name': 'estado'},
        ),
        migrations.AlterField(
            model_name='imovel',
            name='tipo',
            field=models.PositiveIntegerField(default=1, verbose_name=b'tipo de im\xc3\xb3vel', choices=[(1, b'Resid\xc3\xaancia'), (2, b'Com\xc3\xa9rcio'), (3, b'Terreno Baldio'), (4, b'Outros')]),
        ),
        migrations.DeleteModel(
            name='TipoImovel',
        ),
        migrations.AlterField(
            model_name='municipio',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='uf',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='uf',
            name='sigla',
            field=models.CharField(max_length=3),
        ),
    ]
