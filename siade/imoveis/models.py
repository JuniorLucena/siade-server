# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models import Max, F, Count
from djchoices import DjangoChoices, ChoiceItem
from rest_sync import sync_register
from siade.base.models import BaseModel


class UF(BaseModel):
    '''
    Uma Unidade Federativa
    '''
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'estado'
        ordering = ('nome',)


class Municipio(BaseModel):
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


class Bairro(BaseModel):
    '''
    Bairro de um município
    '''
    nome = models.CharField(max_length=100, verbose_name='nome')
    municipio = models.ForeignKey(Municipio, related_name='bairros',
                                  verbose_name='município',
                                  on_delete=models.PROTECT)
    codigo = models.IntegerField(blank=True, null=True,
                                 verbose_name='código')

    def __unicode__(self):
        return "%s" % (self.nome,)

    class Meta:
        ordering = ('municipio', 'nome',)


@sync_register
class Logradouro(BaseModel):
    '''
    Logradouro de um município
    '''
    nome = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, blank=True, null=True,
                                  verbose_name='município',
                                  on_delete=models.PROTECT)

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


@sync_register
class Quadra(BaseModel):
    '''
    Quadra de imóveis de um bairro
    '''
    bairro = models.ForeignKey(Bairro, related_name='quadras',
                               on_delete=models.PROTECT)
    numero = models.PositiveIntegerField(default=0, verbose_name='número')
    sequencia = models.PositiveIntegerField(blank=True, null=True,
                                            verbose_name='sequência')

    def get_numero_display(self):
        if self.sequencia:
            return '%d/%d' % (self.numero, self.sequencia)
        else:
            return '%d' % self.numero

    def __unicode__(self):
       return 'Quadra %s, %s' % (self.get_numero_display(), self.bairro.nome)

    def imoveis_count(self):
        return self.lados.aggregate(t=Count('imoveis')).get('t')

    class Meta:
        ordering = ('bairro', 'numero', 'sequencia')
        unique_together = ('bairro', 'numero', 'sequencia')


@sync_register
class LadoQuadra(BaseModel):
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


@sync_register
class Imovel(BaseModel):
    '''
    Detalhes de um imóvel
    '''
    class Tipo(DjangoChoices):
        '''Possiveis tipos para um imóveis'''
        Residencia = ChoiceItem(1, label='Residência')
        Comercio = ChoiceItem(2, label='Comércio')
        Terreno = ChoiceItem(3, label='Terreno Baldio')
        Outros = ChoiceItem(4, label='Outros')

    ordem = models.PositiveIntegerField(blank=True)
    lado = models.ForeignKey(LadoQuadra, related_name='imoveis',
                             on_delete=models.PROTECT)
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
    qrcode = models.CharField(max_length=32, blank=True, editable=False)

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

    def __init__(self, *args, **kwargs):
        super(Imovel, self).__init__(*args, **kwargs)
        self._old_ordem = self.ordem

    def save(self, *args, **kwargs):
        qs = self._default_manager.filter(lado=self.lado)
        # definir número de ordem não definida
        if self.ordem is None or self.ordem == 0:
            c = qs.aggregate(Max('ordem')).get('ordem__max')
            self.ordem = 1 if c is None else c + 1

        if self.pk:
            # Se estiver atualizando executar apenas se o numero mudar
            if self._old_ordem is not None:
                qs.filter(ordem__gt=self._old_ordem).update(ordem=F('ordem')-1)

        # Se estiver inserindo alterações sequencia dos demais
        qs.filter(ordem__gte=self.ordem).update(ordem=F('ordem')+1)

        super(Imovel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        qs = self._default_manager.filter(lado=self.lado)
        # atualizar ordem ao remover imovel
        qs.filter(ordem__gt=self.ordem).update(ordem=F('ordem')-1)
        super(Imovel, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'imóvel'
        verbose_name_plural = 'imóveis'
        ordering = ('ordem',)
