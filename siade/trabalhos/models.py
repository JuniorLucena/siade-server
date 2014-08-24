# -*- coding: utf-8 -*-
from datetime import date
from django.db import models
from django.utils.translation import gettext as _
from djchoices import DjangoChoices, ChoiceItem
from simple_history.models import HistoricalRecords
from siade.imoveis.models import Imovel, Quadra, Bairro
from siade.agentes.models import Agente


class Ciclo(models.Model):
    '''
    Ciclo de trabalho de um agente em um ciclo
    '''
    data_inicio = models.DateField(verbose_name=_('data inicial'))
    data_fim = models.DateField(verbose_name=_('data final'))
    fechado_em = models.DateField(editable=False, null=True,
                                  verbose_name=_('finalizado em'))
    numero = models.PositiveIntegerField(verbose_name=_('número'))
    ano_base = models.PositiveIntegerField(verbose_name=_('ano base'))
    history = HistoricalRecords()

    def __unicode__(self):
        return '%d/%d' % (self.numero, self.ano_base)

    class Meta:
        verbose_name = _('ciclo')
        verbose_name_plural = _('ciclos')
        ordering = ('-ano_base', '-numero')


class Trabalho(models.Model):
    '''
    Trabalho realizado por um agente em um ciclo
    '''
    agente = models.ForeignKey(Agente, related_name='trabalhos',
                               verbose_name=_('agente'))
    ciclo = models.ForeignKey(Ciclo, related_name='trabalhos',
                              verbose_name=_('ciclo'))
    quadra = models.ForeignKey(Quadra,
                               related_name='trabalhos')
    concluido = models.BooleanField(default=False, editable=False)
    history = HistoricalRecords()

    def __unicode__(self):
        return 'agente %s na quadra %s (ciclo %s)' % (
            self.agente.first_name, self.quadra, self.ciclo)


class Atividade(models.Model):
    '''
    Atividade que pode realizada
    '''
    nome = models.CharField(max_length=100, verbose_name=_('nome'))
    sigla = models.CharField(max_length=5, verbose_name=_('sigla'))

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = _('atividade')
        verbose_name_plural = _('atividades')
        ordering = ('nome',)


class Tratamento(models.Model):
    '''
    Tratamento feito por um agente durante uma visita
    '''
    imovel_tratado = models.NullBooleanField(
        blank=True, null=True, verbose_name=_('imóvel tratado'))
    depositos_tratados = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('depósitos tratados'))
    depositos_eliminados = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('depósitos eliminados'))
    larvicida = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_('larvicida'))
    qtd_larvicida = models.FloatField(
        blank=True, null=True, verbose_name=_('qtd. larvicida'))

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
        blank=True, null=True, verbose_name=_('amostra inicial'))
    amostra_final = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('amostra final'))
    tubitos = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('qtd. tubitos'))

    @property
    def amostra_total(self):
        return self.amostra_final - self.amostra_inicial

    class Meta:
        abstract = True


class Visita(Tratamento, Pesquisa):
    '''
    Visita de um agente a um determinado imovel em um ciclo
    '''
    class Tipo(DjangoChoices):
        '''Possiveis tipos para uma visita'''
        Normal = ChoiceItem(1, label=_('Normal'))
        Recuperada = ChoiceItem(2, label=_('Recuperada'))

    class Pendencia(DjangoChoices):
        '''Possiveis tipos de pendencia para uma visita'''
        Nenhuma = ChoiceItem(0, label=_('Nenhuma'))
        Fechada = ChoiceItem(1, label=_('Fechada'))
        Recusada = ChoiceItem(2, label=_('Recusada'))

    data = models.DateField(default=date.today(), verbose_name=_('data'))
    hora = models.TimeField(verbose_name=_('hora'))
    ciclo = models.ForeignKey(Ciclo, related_name='visitas',
                              verbose_name=_('ciclo'))
    agente = models.ForeignKey(Agente, related_name='visitas',
                               verbose_name=_('agente'))
    imovel = models.ForeignKey(Imovel, related_name='visitas',
                               verbose_name=_('imóvel'))
    atividade = models.ForeignKey(Atividade, related_name='visitas',
                                  verbose_name=_('atividade'))
    tipo = models.PositiveIntegerField(choices=Tipo.choices,
                                       default=Tipo.Normal,
                                       verbose_name=_('tipo'))
    pendencia = models.PositiveIntegerField(choices=Pendencia.choices,
                                            default=Pendencia.Nenhuma,
                                            verbose_name=_('pendencia'))
    history = HistoricalRecords()

    class Meta:
        verbose_name = _('visita')
        verbose_name_plural = _('visitas')
        ordering = ('data', 'hora', 'ciclo')
