# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True)),
                ('data_inicio', models.DateField(verbose_name='data inicial')),
                ('data_fim', models.DateField(verbose_name='data final')),
                ('fechado_em', models.DateField(verbose_name='finalizado em', null=True, editable=False)),
                ('atividade', models.PositiveIntegerField(choices=[(1, 'Levantamento de \xcdndice (LI)'), (1, 'Tratamento (T)'), (1, 'Levantamento de \xcdndice + Tratamento (LI+T)')])),
                ('numero', models.PositiveIntegerField(verbose_name='n\xfamero')),
                ('ano_base', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('-ano_base', '-numero'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True)),
                ('concluido', models.BooleanField(default=False, editable=False)),
                ('agente', models.ForeignKey(related_name='trabalhos', to=settings.AUTH_USER_MODEL)),
                ('ciclo', models.ForeignKey(related_name='trabalhos', to='trabalhos.Ciclo')),
                ('quadra', models.ForeignKey(related_name='trabalhos', to='imoveis.Quadra')),
            ],
            options={
                'ordering': ('agente', 'ciclo', 'quadra__id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True)),
                ('imovel_tratado', models.NullBooleanField(verbose_name='im\xf3vel tratado')),
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
                ('amostra_inicial', models.PositiveIntegerField(null=True, verbose_name='amostra inicial', blank=True)),
                ('amostra_final', models.PositiveIntegerField(null=True, verbose_name='amostra final', blank=True)),
                ('tubitos', models.PositiveIntegerField(null=True, verbose_name='qtd. tubitos', blank=True)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('imovel_inspecionado', models.NullBooleanField(verbose_name='im\xf3vel inspecionado')),
                ('tipo', models.PositiveIntegerField(default=1, choices=[(1, 'Normal'), (2, 'Recuperada')])),
                ('pendencia', models.PositiveIntegerField(default=1, verbose_name='pend\xeancia', choices=[(1, 'Nenhuma'), (2, 'Fechada'), (3, 'Recusada')])),
                ('agente', models.ForeignKey(related_name='visitas', to=settings.AUTH_USER_MODEL)),
                ('ciclo', models.ForeignKey(related_name='visitas', to='trabalhos.Ciclo')),
                ('imovel', models.ForeignKey(related_name='visitas', verbose_name='im\xf3vel', to='imoveis.Imovel')),
            ],
            options={
                'ordering': ('data', 'hora', 'ciclo'),
                'verbose_name': 'visita',
                'verbose_name_plural': 'visitas',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='visita',
            unique_together=set([('ciclo', 'agente', 'imovel')]),
        ),
        migrations.AlterUniqueTogether(
            name='trabalho',
            unique_together=set([('ciclo', 'quadra')]),
        ),
    ]
