# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'nome')),
                ('sigla', models.CharField(max_length=5, verbose_name=b'sigla')),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_inicio', models.DateField(verbose_name=b'data inicial')),
                ('data_fim', models.DateField(verbose_name=b'data final')),
                ('fechado_em', models.DateField(verbose_name=b'finalizado em', null=True, editable=False)),
                ('numero', models.PositiveIntegerField(verbose_name=b'n\xc3\xbamero')),
                ('ano_base', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('-ano_base', '-numero'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalCiclo',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('data_inicio', models.DateField(verbose_name=b'data inicial')),
                ('data_fim', models.DateField(verbose_name=b'data final')),
                ('fechado_em', models.DateField(verbose_name=b'finalizado em', null=True, editable=False)),
                ('numero', models.PositiveIntegerField(verbose_name=b'n\xc3\xbamero')),
                ('ano_base', models.PositiveIntegerField()),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical ciclo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalTrabalho',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('agente_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('ciclo_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('quadra_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('concluido', models.BooleanField(default=False, editable=False)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical trabalho',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalVisita',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('imovel_tratado', models.NullBooleanField(verbose_name=b'im\xc3\xb3vel tratado')),
                ('depositos_tratados', models.PositiveIntegerField(null=True, blank=True)),
                ('depositos_eliminados', models.PositiveIntegerField(null=True, blank=True)),
                ('larvicida', models.CharField(max_length=50, null=True, blank=True)),
                ('qtd_larvicida', models.FloatField(null=True, blank=True)),
                ('A1', models.PositiveIntegerField(null=True, blank=True)),
                ('A2', models.PositiveIntegerField(null=True, blank=True)),
                ('B', models.PositiveIntegerField(null=True, blank=True)),
                ('C', models.PositiveIntegerField(null=True, blank=True)),
                ('D1', models.PositiveIntegerField(null=True, blank=True)),
                ('D2', models.PositiveIntegerField(null=True, blank=True)),
                ('E', models.PositiveIntegerField(null=True, blank=True)),
                ('amostra_inicial', models.PositiveIntegerField(null=True, verbose_name=b'amostra inicial', blank=True)),
                ('amostra_final', models.PositiveIntegerField(null=True, verbose_name=b'amostra final', blank=True)),
                ('tubitos', models.PositiveIntegerField(null=True, verbose_name=b'qtd. tubitos', blank=True)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('ciclo_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('agente_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('imovel_id', models.IntegerField(db_index=True, null=True, verbose_name=b'im\xc3\xb3vel', blank=True)),
                ('atividade_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('tipo', models.PositiveIntegerField(default=1, choices=[(1, b'Normal'), (2, b'Recuperada')])),
                ('pendencia', models.PositiveIntegerField(default=0, verbose_name=b'pend\xc3\xaancia', choices=[(b'Nenhuma', b'Nenhuma'), (1, b'Fechada'), (2, b'Recusada')])),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical visita',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concluido', models.BooleanField(default=False, editable=False)),
                ('agente', models.ForeignKey(related_name=b'trabalhos', to='agentes.Agente')),
                ('ciclo', models.ForeignKey(related_name=b'trabalhos', to='trabalhos.Ciclo')),
                ('quadra', models.ForeignKey(related_name=b'trabalhos', to='imoveis.Quadra')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imovel_tratado', models.NullBooleanField(verbose_name=b'im\xc3\xb3vel tratado')),
                ('depositos_tratados', models.PositiveIntegerField(null=True, blank=True)),
                ('depositos_eliminados', models.PositiveIntegerField(null=True, blank=True)),
                ('larvicida', models.CharField(max_length=50, null=True, blank=True)),
                ('qtd_larvicida', models.FloatField(null=True, blank=True)),
                ('A1', models.PositiveIntegerField(null=True, blank=True)),
                ('A2', models.PositiveIntegerField(null=True, blank=True)),
                ('B', models.PositiveIntegerField(null=True, blank=True)),
                ('C', models.PositiveIntegerField(null=True, blank=True)),
                ('D1', models.PositiveIntegerField(null=True, blank=True)),
                ('D2', models.PositiveIntegerField(null=True, blank=True)),
                ('E', models.PositiveIntegerField(null=True, blank=True)),
                ('amostra_inicial', models.PositiveIntegerField(null=True, verbose_name=b'amostra inicial', blank=True)),
                ('amostra_final', models.PositiveIntegerField(null=True, verbose_name=b'amostra final', blank=True)),
                ('tubitos', models.PositiveIntegerField(null=True, verbose_name=b'qtd. tubitos', blank=True)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('tipo', models.PositiveIntegerField(default=1, choices=[(1, b'Normal'), (2, b'Recuperada')])),
                ('pendencia', models.PositiveIntegerField(default=0, verbose_name=b'pend\xc3\xaancia', choices=[(b'Nenhuma', b'Nenhuma'), (1, b'Fechada'), (2, b'Recusada')])),
                ('agente', models.ForeignKey(related_name=b'visitas', to='agentes.Agente')),
                ('atividade', models.ForeignKey(related_name=b'visitas', to='trabalhos.Atividade')),
                ('ciclo', models.ForeignKey(related_name=b'visitas', to='trabalhos.Ciclo')),
                ('imovel', models.ForeignKey(related_name=b'visitas', verbose_name=b'im\xc3\xb3vel', to='imoveis.Imovel')),
            ],
            options={
                'ordering': ('data', 'hora', 'ciclo'),
                'verbose_name': 'visita',
                'verbose_name_plural': 'visitas',
            },
            bases=(models.Model,),
        ),
    ]
