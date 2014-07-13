# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext as _

class UF(models.Model):
	'''
	Uma Unidade Federativa
	'''
	nome = models.CharField(max_length=100, verbose_name=_('nome'))
	sigla = models.CharField(max_length=3, verbose_name=_('sigla'))

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name = _('estado')
		verbose_name_plural = _('estados')

class Municipio(models.Model):
	'''
	Município de uma UF
	'''
	nome = models.CharField(max_length=100, verbose_name=_('nome'))
	uf = models.ForeignKey(UF, verbose_name=_('UF'))
	codigo = models.IntegerField(blank=True, null=True, verbose_name=_('código'))

	def __unicode__(self):
		return "%s, %s" % (self.nome, self.uf.sigla)

	class Meta:
		verbose_name = _('município')
		verbose_name_plural = _('municípios')

class Bairro(models.Model):
	'''
	Bairro de um município
	'''
	nome = models.CharField(max_length=100, verbose_name=_('nome'))
	municipio = models.ForeignKey(Municipio, related_name='bairros', verbose_name=_('Município'))
	codigo = models.IntegerField(blank=True, null=True, verbose_name=_('código'))

	def __unicode__(self):
		return "%s" % (self.nome,)

	class Meta:
		verbose_name = _('bairro')
		verbose_name_plural = _('bairros')
		ordering = ('municipio',)

class Logradouro(models.Model):
	'''
	Logradouro de um município
	'''
	nome = models.CharField(max_length=100, verbose_name=_('nome'))
	municipio = models.ForeignKey(Municipio, blank=True, null=True, verbose_name=_('município'))

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name = _('logradouro')
		verbose_name_plural = _('logradouros')
		ordering = ('nome',)

class Quadra(models.Model):
	'''
	Quadra de imóveis de um bairro
	'''
	bairro = models.ForeignKey(Bairro, related_name='quadras', verbose_name=_('bairro'))
	numero = models.CharField(max_length=10, verbose_name=_('número'))

	def imoveis_count(self):
		return Imovel.objects.filter(lado__quadra=self.pk).count()

	def __unicode__(self):
		return "%s quadra #%s" % (self.bairro.nome, self.numero)
	
	class Meta:
		verbose_name = _('quadra')
		verbose_name_plural = _('quadras')
		ordering = ('bairro', 'numero')

class LadoQuadra(models.Model):
	'''
	Lado de uma quadra
	'''
	numero = models.PositiveIntegerField(verbose_name=_('número'), blank=True, null=True)
	quadra = models.ForeignKey(Quadra, verbose_name=_('quadra'), related_name='lados')
	logradouro = models.ForeignKey(Logradouro, verbose_name=_('logradouro'))

	def __unicode__(self):
		return '%s, %s' % (self.logradouro.nome, self.quadra)

	@property
	def imoveis_total(self):
		return self.imoveis.count()

	class Meta:
		verbose_name = _('lado de quadra')
		verbose_name_plural = _('lados de quadra')
		ordering = ('numero',)

class TipoImovel(models.Model):
	'''
	Tipo de imóvel
	'''
	nome = models.CharField(max_length=100, verbose_name=_('nome'))
	sigla = models.CharField(max_length=3, verbose_name=_('sigla'))

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name = _('tipo de imóvel')
		verbose_name_plural = _('tipos de imóvel')
		ordering = ('nome',)

class Imovel(models.Model):
	'''
	Detalhes de um imóvel
	'''
	lado = models.ForeignKey(LadoQuadra, related_name='imoveis')
	numero = models.CharField(max_length=10, blank=True, verbose_name=_('número'))
	tipo = models.ForeignKey(TipoImovel, verbose_name=_('tipo de imóvel'))
	habitantes = models.PositiveIntegerField(verbose_name=_('qtd. habitantes'))
	caes = models.PositiveIntegerField(verbose_name=_('qtd. cães'))
	gatos = models.PositiveIntegerField(verbose_name=_('qtd. gatos'))
	ordem = models.PositiveIntegerField(verbose_name=_('ordem'), editable=False, null=True)

	def __unicode__(self):
		numero = 'S/N' if bool(self.numero) == False else self.numero
		return "%s, %s" % (self.lado.logradouro.nome, numero)

	@property
	def endereco(self):
		numero = 'S/N' if bool(self.numero) == False else self.numero
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
		verbose_name = _('imóvel')
		verbose_name_plural = _('imóveis')
		ordering = ('numero',)