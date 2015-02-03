# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0005_auto_20150109_2235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imovel',
            options={'ordering': ('ordem',), 'verbose_name': 'im\xf3vel', 'verbose_name_plural': 'im\xf3veis'},
        ),
        migrations.AlterField(
            model_name='bairro',
            name='codigo',
            field=models.IntegerField(null=True, verbose_name='c\xf3digo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bairro',
            name='municipio',
            field=models.ForeignKey(related_name='bairros', on_delete=django.db.models.deletion.PROTECT, verbose_name='Munic\xedpio', to='imoveis.Municipio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imovel',
            name='caes',
            field=models.PositiveIntegerField(default=0, verbose_name='qtd. c\xe3es'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imovel',
            name='numero',
            field=models.CharField(max_length=10, verbose_name='n\xfamero', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imovel',
            name='ordem',
            field=models.PositiveIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imovel',
            name='ponto_estrategico',
            field=models.BooleanField(default=False, verbose_name='ponto estrat\xe9gico'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imovel',
            name='tipo',
            field=models.PositiveIntegerField(default=1, verbose_name='tipo de im\xf3vel', choices=[(1, 'Resid\xeancia'), (2, 'Com\xe9rcio'), (3, 'Terreno Baldio'), (4, 'Outros')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ladoquadra',
            name='numero',
            field=models.PositiveIntegerField(null=True, verbose_name='n\xfamero', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logradouro',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='munic\xedpio', blank=True, to='imoveis.Municipio', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='municipio',
            name='codigo',
            field=models.IntegerField(null=True, verbose_name='c\xf3digo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quadra',
            name='numero',
            field=models.CharField(max_length=10, verbose_name='n\xfamero'),
            preserve_default=True,
        ),
    ]
