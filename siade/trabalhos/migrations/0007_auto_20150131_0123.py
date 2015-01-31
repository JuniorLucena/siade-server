# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0006_auto_20150131_0120'),
        ('trabalhos', '0006_auto_20150108_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabalho',
            name='quadras',
        ),
        migrations.AddField(
            model_name='trabalho',
            name='quadra',
            field=models.ForeignKey(related_name='trabalhos', default=0, to='imoveis.Quadra'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ciclo',
            name='numero',
            field=models.PositiveIntegerField(verbose_name='n\xfamero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visita',
            name='imovel',
            field=models.ForeignKey(related_name='visitas', verbose_name='im\xf3vel', to='imoveis.Imovel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visita',
            name='imovel_tratado',
            field=models.NullBooleanField(verbose_name='im\xf3vel tratado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visita',
            name='pendencia',
            field=models.PositiveIntegerField(default=0, verbose_name='pend\xeancia', choices=[('Nenhuma', 'Nenhuma'), (1, 'Fechada'), (2, 'Recusada')]),
            preserve_default=True,
        ),
    ]
