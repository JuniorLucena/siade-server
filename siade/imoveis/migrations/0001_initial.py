# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'nome')),
                ('codigo', models.IntegerField(null=True, verbose_name=b'c\xc3\xb3digo', blank=True)),
            ],
            options={
                'ordering': ('municipio',),
                'verbose_name': 'bairro',
                'verbose_name_plural': 'bairros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalBairro',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'nome')),
                ('municipio_id', models.IntegerField(db_index=True, null=True, verbose_name=b'Munic\xc3\xadpio', blank=True)),
                ('codigo', models.IntegerField(null=True, verbose_name=b'c\xc3\xb3digo', blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical bairro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalImovel',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('ordem', models.PositiveIntegerField()),
                ('lado_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('numero', models.CharField(max_length=10, verbose_name=b'n\xc3\xbamero', blank=True)),
                ('tipo_id', models.IntegerField(db_index=True, null=True, verbose_name=b'tipo de im\xc3\xb3vel', blank=True)),
                ('habitantes', models.PositiveIntegerField(verbose_name=b'qtd. habitantes')),
                ('caes', models.PositiveIntegerField(default=0, verbose_name=b'qtd. c\xc3\xa3es')),
                ('gatos', models.PositiveIntegerField(default=0, verbose_name=b'qtd. gatos')),
                ('ponto_estrategico', models.BooleanField(default=False, verbose_name=b'ponto estrat\xc3\xa9gico')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical im\xf3vel',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalLadoQuadra',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('numero', models.PositiveIntegerField(null=True, verbose_name=b'n\xc3\xbamero', blank=True)),
                ('quadra_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('logradouro_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical lado de quadra',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalLogradouro',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('nome', models.CharField(max_length=100)),
                ('municipio_id', models.IntegerField(db_index=True, null=True, verbose_name=b'munic\xc3\xadpio', blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical logradouro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalQuadra',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('bairro_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('numero', models.CharField(max_length=10, verbose_name=b'n\xc3\xbamero')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical quadra',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalTipoImovel',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'nome')),
                ('sigla', models.CharField(max_length=3, verbose_name=b'sigla')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical tipo de im\xf3vel',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordem', models.PositiveIntegerField()),
                ('numero', models.CharField(max_length=10, verbose_name=b'n\xc3\xbamero', blank=True)),
                ('habitantes', models.PositiveIntegerField(verbose_name=b'qtd. habitantes')),
                ('caes', models.PositiveIntegerField(default=0, verbose_name=b'qtd. c\xc3\xa3es')),
                ('gatos', models.PositiveIntegerField(default=0, verbose_name=b'qtd. gatos')),
                ('ponto_estrategico', models.BooleanField(default=False, verbose_name=b'ponto estrat\xc3\xa9gico')),
            ],
            options={
                'ordering': ('numero',),
                'verbose_name': 'im\xf3vel',
                'verbose_name_plural': 'im\xf3veis',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LadoQuadra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(null=True, verbose_name=b'n\xc3\xbamero', blank=True)),
            ],
            options={
                'ordering': ('numero',),
                'verbose_name': 'lado de quadra',
                'verbose_name_plural': 'lados de quadra',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'logradouro',
                'verbose_name_plural': 'logradouros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'nome')),
                ('codigo', models.IntegerField(null=True, verbose_name=b'c\xc3\xb3digo', blank=True)),
            ],
            options={
                'verbose_name': 'munic\xedpio',
                'verbose_name_plural': 'munic\xedpios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=10, verbose_name=b'n\xc3\xbamero')),
                ('bairro', models.ForeignKey(related_name=b'quadras', to='imoveis.Bairro')),
            ],
            options={
                'ordering': ('bairro', 'numero'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoImovel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'nome')),
                ('sigla', models.CharField(max_length=3, verbose_name=b'sigla')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'tipo de im\xf3vel',
                'verbose_name_plural': 'tipos de im\xf3vel',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'nome')),
                ('sigla', models.CharField(max_length=3, verbose_name=b'sigla')),
            ],
            options={
                'verbose_name': 'estado',
                'verbose_name_plural': 'estados',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='municipio',
            name='uf',
            field=models.ForeignKey(verbose_name=b'UF', to='imoveis.UF'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logradouro',
            name='municipio',
            field=models.ForeignKey(verbose_name=b'munic\xc3\xadpio', blank=True, to='imoveis.Municipio', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ladoquadra',
            name='logradouro',
            field=models.ForeignKey(to='imoveis.Logradouro', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ladoquadra',
            name='quadra',
            field=models.ForeignKey(related_name=b'lados', to='imoveis.Quadra'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imovel',
            name='lado',
            field=models.ForeignKey(related_name=b'imoveis', to='imoveis.LadoQuadra'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imovel',
            name='tipo',
            field=models.ForeignKey(verbose_name=b'tipo de im\xc3\xb3vel', to='imoveis.TipoImovel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bairro',
            name='municipio',
            field=models.ForeignKey(related_name=b'bairros', verbose_name=b'Munic\xc3\xadpio', to='imoveis.Municipio'),
            preserve_default=True,
        ),
    ]
