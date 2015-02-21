# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('imoveis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', django_extensions.db.fields.ShortUUIDField(serialize=False, editable=False, primary_key=True, blank=True)),
                ('cpf', models.BigIntegerField(unique=True, verbose_name='CPF')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75, verbose_name='e-mail', blank=True)),
                ('telefone', models.BigIntegerField(null=True, blank=True)),
                ('nascimento', models.DateField(null=True, verbose_name='data de nasc.', blank=True)),
                ('codigo', models.CharField(unique=True, max_length=20, verbose_name='c\xf3digo')),
                ('tipo', models.PositiveIntegerField(default=1, choices=[(1, 'Agente de campo'), (2, 'Supervisor'), (99, 'Administrador')])),
                ('ativo', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('municipio', models.ForeignKey(blank=True, to='imoveis.Municipio', null=True)),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'agente',
                'verbose_name_plural': 'agentes',
            },
            bases=(models.Model,),
        ),
    ]
