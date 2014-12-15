# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext as _
from djchoices import DjangoChoices, ChoiceItem


class UF(models.Model):
    '''
    Uma Unidade Federativa
    '''
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'estado'


class Municipio(models.Model):
    '''
    Município de uma UF
    '''
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, verbose_name='UF')
    codigo = models.IntegerField(
        blank=True, null=True, verbose_name='código')

    def __unicode__(self):
        return "%s, %s" % (self.nome, self.uf.sigla)

    class Meta:
        verbose_name = 'município'


class Bairro(models.Model):
    '''
    Bairro de um município
    '''
    nome = models.CharField(max_length=100, verbose_name=_('nome'))
    municipio = models.ForeignKey(Municipio, related_name='bairros',
                                  verbose_name=_('Município'))
    codigo = models.IntegerField(blank=True, null=True,
                                 verbose_name=_('código'))

    def __unicode__(self):
        return "%s" % (self.nome,)

    class Meta:
        ordering = ('municipio',)


class Logradouro(models.Model):
    '''
    Logradouro de um município
    '''
    nome = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, blank=True, null=True,
                                  verbose_name='município')

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Quadra(models.Model):
    '''
    Quadra de imóveis de um bairro
    '''
    bairro = models.ForeignKey(Bairro, related_name='quadras')
    numero = models.CharField(max_length=10, verbose_name='número')

    def __unicode__(self):
        return 'Quadra #%s, %s' % (self.numero, self.bairro.nome)

    class Meta:
        ordering = ('bairro', 'numero')
        unique_together = ('bairro', 'numero')


class LadoQuadra(models.Model):
    '''
    Lado de uma quadra
    '''
    numero = models.PositiveIntegerField(blank=True, null=True,
                                         verbose_name='número')
    quadra = models.ForeignKey(Quadra, related_name='lados')
    logradouro = models.ForeignKey(Logradouro, null=True)

    def __unicode__(self):
        return 'Lado %d, %s' % (self.numero, self.quadra)

    @property
    def imoveis_total(self):
        return self.imoveis.count()

    class Meta:
        verbose_name = 'lado de quadra'
        verbose_name_plural = 'lados de quadra'
        ordering = ('numero',)
        unique_together = ('quadra', 'numero')


class Imovel(models.Model):
    '''
    Detalhes de um imóvel
    '''
    class Tipo(DjangoChoices):
        '''Possiveis tipos para um imóveis'''
        Residencia = ChoiceItem(1, label='Residência')
        Comercio = ChoiceItem(2, label='Comércio')
        Terreno = ChoiceItem(3, label='Terreno Baldio')
        Outros = ChoiceItem(4, label='Outros')

    ordem = models.PositiveIntegerField()
    lado = models.ForeignKey(LadoQuadra, related_name='imoveis')
    numero = models.CharField(max_length=10, blank=True,
                              verbose_name='número')
    tipo = models.PositiveIntegerField(choices=Tipo.choices,
                                       default=Tipo.Residencia,
                                       verbose_name='tipo de imóvel')
    habitantes = models.PositiveIntegerField(verbose_name='qtd. habitantes')
    caes = models.PositiveIntegerField(default=0, verbose_name='qtd. cães')
    gatos = models.PositiveIntegerField(default=0, verbose_name='qtd. gatos')
    ponto_estrategico = models.BooleanField(default=False,
                                            verbose_name='ponto estratégico')

    def __unicode__(self):
        numero = self.numero if bool(self.numero) else 'S/N'
        return "%s, %s" % (self.lado.logradouro.nome, numero)

    @property
    def endereco(self):
        numero = self.numero if bool(self.numero) else 'S/N'
        logradouro = self.lado.logradouro.nome
        bairro = self.lado.quadra.bairro
        return "%s, %s, %s" % (logradouro, numero, bairro)

    @property
    def quadra(self):
        return self.lado_quadra.quadra

    @property
    def logradouro(self):
        return self.lado_quadra.logradouro

    class Meta:
        verbose_name = 'imovel'
        verbose_name_plural = 'imóveis'
        ordering = ('ordem',)
        unique_together = ('lado', 'ordem')
