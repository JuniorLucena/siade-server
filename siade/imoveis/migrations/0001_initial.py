# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', django_extensions.db.fields.UUIDField(serialize=False, editable=False, primary_key=True, blank=True)),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('codigo', models.IntegerField(null=True, verbose_name='c\xf3digo', blank=True)),
            ],
            options={
                'ordering': ('municipio',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', django_extensions.db.fields.UUIDField(serialize=False, editable=False, primary_key=True, blank=True)),
                ('ordem', models.PositiveIntegerField(blank=True)),
                ('numero', models.CharField(max_length=10, verbose_name='n\xfamero', blank=True)),
                ('tipo', models.PositiveIntegerField(default=1, verbose_name='tipo de im\xf3vel', choices=[(1, 'Resid\xeancia'), (2, 'Com\xe9rcio'), (3, 'Terreno Baldio'), (4, 'Outros')])),
                ('habitantes', models.PositiveIntegerField(verbose_name='qtd. habitantes')),
                ('caes', models.PositiveIntegerField(default=0, verbose_name='qtd. c\xe3es')),
                ('gatos', models.PositiveIntegerField(default=0, verbose_name='qtd. gatos')),
                ('ponto_estrategico', models.BooleanField(default=False, verbose_name='ponto estrat\xe9gico')),
            ],
            options={
                'ordering': ('ordem',),
                'verbose_name': 'im\xf3vel',
                'verbose_name_plural': 'im\xf3veis',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LadoQuadra',
            fields=[
                ('id', django_extensions.db.fields.UUIDField(serialize=False, editable=False, primary_key=True, blank=True)),
                ('numero', models.PositiveIntegerField(null=True, verbose_name='n\xfamero', blank=True)),
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
                ('id', django_extensions.db.fields.UUIDField(serialize=False, editable=False, primary_key=True, blank=True)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', django_extensions.db.fields.UUIDField(serialize=False, editable=False, primary_key=True, blank=True)),
                ('nome', models.CharField(max_length=100)),
                ('codigo', models.IntegerField(null=True, verbose_name='c\xf3digo', blank=True)),
            ],
            options={
                'verbose_name': 'munic\xedpio',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', django_extensions.db.fields.UUIDField(serialize=False, editable=False, primary_key=True, blank=True)),
                ('numero', models.PositiveIntegerField(default=0, verbose_name='n\xfamero')),
                ('bairro', models.ForeignKey(related_name='quadras', on_delete=django.db.models.deletion.PROTECT, to='imoveis.Bairro')),
            ],
            options={
                'ordering': ('bairro', 'numero'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id', django_extensions.db.fields.UUIDField(serialize=False, editable=False, primary_key=True, blank=True)),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'estado',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='quadra',
            unique_together=set([('bairro', 'numero')]),
        ),
        migrations.AddField(
            model_name='municipio',
            name='uf',
            field=models.ForeignKey(verbose_name='UF', to='imoveis.UF'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logradouro',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='munic\xedpio', blank=True, to='imoveis.Municipio', null=True),
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
            field=models.ForeignKey(related_name='lados', to='imoveis.Quadra'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='ladoquadra',
            unique_together=set([('quadra', 'numero')]),
        ),
        migrations.AddField(
            model_name='imovel',
            name='lado',
            field=models.ForeignKey(related_name='imoveis', on_delete=django.db.models.deletion.PROTECT, to='imoveis.LadoQuadra'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bairro',
            name='municipio',
            field=models.ForeignKey(related_name='bairros', on_delete=django.db.models.deletion.PROTECT, verbose_name='munic\xedpio', to='imoveis.Municipio'),
            preserve_default=True,
        ),
    ]
