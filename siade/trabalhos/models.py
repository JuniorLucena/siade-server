# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from rest_sync import sync_register
from siade.base.models import BaseModel
from siade.imoveis.models import Imovel, Quadra
from siade.agentes.models import Agente


class CicloAtualManager(models.Manager):
    '''
    Model manager que filtra o resultados pelo ciclo atual
    '''
    use_for_related_fields = True

    def get_queryset(self):
        return super(CicloAtualManager, self).get_queryset().filter(
            ciclo=Ciclo.atual())


class Ciclo(BaseModel):
    '''
    Ciclo de trabalho de um agente em um ciclo
    '''
    class Atividade(DjangoChoices):
        ''' Tipos de atividade possiveis para ciclo '''
        LI = ChoiceItem(1, label='Levantamento de Índice (LI)')
        T = ChoiceItem(2, label='Tratamento (T)')
        LIT = ChoiceItem(3, label='Levantamento de Índice + Tratamento (LI+T)')

    data_inicio = models.DateField(verbose_name='data inicial')
    data_fim = models.DateField(verbose_name='data final')
    fechado_em = models.DateField(editable=False, null=True,
                                  verbose_name='finalizado em')
    atividade = models.PositiveIntegerField(choices=Atividade.choices)
    numero = models.PositiveIntegerField(verbose_name='número')
    ano_base = models.PositiveIntegerField()

    def __unicode__(self):
        return '%d/%d' % (self.numero, self.ano_base)

    @staticmethod
    def atual():
        ''' Pegar o último ciclo aberto '''
        return Ciclo.objects.first()

    class Meta:
        ordering = ('-ano_base', '-numero')


class Trabalho(BaseModel):
    '''
    Trabalho realizado por um agente em um ciclo
    '''
    agente = models.ForeignKey(Agente, related_name='trabalhos')
    ciclo = models.ForeignKey(Ciclo, related_name='trabalhos')
    quadra = models.ForeignKey(Quadra, related_name='trabalhos')
    concluido = models.BooleanField(default=False, editable=False)

    objects = CicloAtualManager()

    def __unicode__(self):
        return '%s, quadra %s, ciclo %s' % (
            self.agente.first_name, self.quadra, self.ciclo)

    class Meta:
        unique_together = ('ciclo', 'quadra')
        ordering = ('agente', 'ciclo', 'quadra__bairro__nome',
                    'quadra__numero')


class Tratamento(models.Model):
    '''
    Tratamento feito por um agente durante uma visita
    '''
    imovel_tratado = models.NullBooleanField(
        blank=True, null=True, verbose_name='imóvel tratado')
    depositos_tratados = models.PositiveIntegerField(
        blank=True, null=True)
    depositos_eliminados = models.PositiveIntegerField(
        blank=True, null=True)
    larvicida = models.CharField(
        max_length=50, blank=True, null=True)
    qtd_larvicida = models.FloatField(
        blank=True, null=True)

    class Meta:
        abstract = True


class Pesquisa(models.Model):
    '''
    Pesquisa feita por um agente durante uma visita
    '''
    A1 = models.PositiveIntegerField(blank=True, null=True)
    A2 = models.PositiveIntegerField(blank=True, null=True)
    B = models.PositiveIntegerField(blank=True, null=True)
    C = models.PositiveIntegerField(blank=True, null=True)
    D1 = models.PositiveIntegerField(blank=True, null=True)
    D2 = models.PositiveIntegerField(blank=True, null=True)
    E = models.PositiveIntegerField(blank=True, null=True)
    amostra_inicial = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='amostra inicial')
    amostra_final = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='amostra final')
    tubitos = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='qtd. tubitos')

    @property
    def amostra_total(self):
        return self.amostra_final - self.amostra_inicial

    class Meta:
        abstract = True


@sync_register
class Visita(BaseModel, Tratamento, Pesquisa):
    '''
    Visita de um agente a um determinado imovel em um ciclo
    '''
    class Tipo(DjangoChoices):
        ''' Possiveis tipos para uma visita '''
        Normal = ChoiceItem(1, label='Normal')
        Recuperada = ChoiceItem(2, label='Recuperada')

    class Pendencia(DjangoChoices):
        ''' Possiveis tipos de pendencia para uma visita '''
        Nenhuma = ChoiceItem(1, label='Nenhuma')
        Fechada = ChoiceItem(2, label='Fechada')
        Recusada = ChoiceItem(3, label='Recusada')

    data = models.DateField()
    hora = models.TimeField()
    ciclo = models.ForeignKey(Ciclo, related_name='visitas')
    agente = models.ForeignKey(Agente, related_name='visitas')
    imovel = models.ForeignKey(Imovel, related_name='visitas',
                               verbose_name='imóvel')
    imovel_inspecionado = models.NullBooleanField(
        blank=True, null=True, verbose_name='imóvel inspecionado')
    tipo = models.PositiveIntegerField(choices=Tipo.choices,
                                       default=Tipo.Normal)
    pendencia = models.PositiveIntegerField(choices=Pendencia.choices,
                                            default=Pendencia.Nenhuma,
                                            verbose_name='pendência')
    objects = CicloAtualManager()

    class Meta:
        verbose_name = 'visita'
        verbose_name_plural = 'visitas'
        ordering = ('data', 'hora', 'ciclo')
        unique_together = ('ciclo', 'agente', 'imovel')
