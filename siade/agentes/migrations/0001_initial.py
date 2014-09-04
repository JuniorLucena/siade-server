# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('cpf', models.BigIntegerField(verbose_name=b'CPF')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75, verbose_name=b'e-mail', blank=True)),
                ('telefone', models.BigIntegerField(null=True, blank=True)),
                ('nascimento', models.DateField(null=True, verbose_name=b'data de nasc.', blank=True)),
                ('codigo', models.CharField(unique=True, max_length=20, verbose_name=b'c\xc3\xb3digo', blank=True)),
                ('tipo', models.PositiveIntegerField(default=1, choices=[(1, b'Agente de campo'), (2, b'Supervisor'), (99, b'Administrador')])),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'agente',
                'verbose_name_plural': 'agentes',
            },
            bases=(models.Model,),
        ),
    ]
