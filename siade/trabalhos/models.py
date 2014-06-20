# -*- coding: utf-8 -*-
from datetime import date
from django.db import models
from django.utils.translation import gettext as _
from djchoices import DjangoChoices, ChoiceItem
from siade.imoveis.models import Imovel, Quadra, Bairro

from django.contrib.auth import get_user_model
User = get_user_model()

class Agente(User):
	'''
	Um agente de endemias
	'''
	def __unicode__(self):
		return self.get_short_name()

	class Meta:
		verbose_name = _('agente')
		verbose_name_plural = _('agentes')

class Campanha(models.Model):
	'''
	Campanha de combate a endemia
	'''
	nome = models.CharField(max_length=100, verbose_name=_('nome'))

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name = _('campanha')
		verbose_name_plural = _('campanhas')
		ordering = ('nome',)

class Ciclo(models.Model):
	''' 
	Ciclo de combate a uma endemia
	'''
	data_inicio = models.DateField(verbose_name=_('data inicial'))
	data_fim = models.DateField(verbose_name=_('data final'))
	numero = models.PositiveIntegerField(verbose_name=_('número'))
	ano_base = models.PositiveIntegerField(verbose_name=_('ano base'))

	def __unicode__(self):
		return '%d/%d' % (self.numero, self.ano_base)

	def distribuir_trabalhos(self):
		pass

	class Meta:
		verbose_name = _('ciclo')
		verbose_name_plural = _('ciclos')
		ordering = ('-ano_base', '-numero')

class Trabalho(models.Model):
	'''
	Trabalho realizado em um ciclo por um agente
	'''
	agente = models.ForeignKey(Agente, related_name='trabalhos', verbose_name=_('agente'))
	campanha = models.ForeignKey(Campanha, related_name='trabalhos', verbose_name=_('campanha'))
	ciclo = models.ForeignKey(Ciclo, related_name='trabalhos', verbose_name=_('ciclo'))
	quadra = models.ForeignKey(Quadra, related_name='trabalhos')
	concluido = models.BooleanField(default=False, editable=False)

	def __unicode__(self):
		return "agente %s, ciclo %s, quadra %s" % (self.agente.first_name, self.ciclo, self.quadra)

	@property
	def bairros(self):
		return Bairro.objects.filter(quadras__trabalhos=self.id).values('bairro').distinct()

	@property
	def imoveis(self):
		return Imovel.objects.filter(lado__quadra__trabalhos=self.id)

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

class Visita(models.Model):
	'''
	Visita de um agente a um determinado imovel em um ciclo
	'''
	class Tipo(DjangoChoices):
		Normal = ChoiceItem(1, label=_('Normal'))
		Recuperada = ChoiceItem(2, label=_('Recuperada'))

	class Pendencia(DjangoChoices):
		Nenhuma = ChoiceItem(0, label=_('Nenhuma'))
		Fechada = ChoiceItem(1, label=_('Fechada'))
		Recusada = ChoiceItem(2, label=_('Recusada'))

	data = models.DateField(default=date.today(), verbose_name=_('data'))
	hora = models.TimeField(verbose_name=_('hora'))
	ciclo = models.ForeignKey(Ciclo, related_name='visitas', verbose_name=_('ciclo'))
	agente = models.ForeignKey(Agente, related_name='visitas', verbose_name=_('agente'))
	imovel = models.ForeignKey(Imovel, related_name='visitas', verbose_name=_('imóvel'))
	atividade = models.ForeignKey(Atividade, related_name='visitas', verbose_name=_('atividade'))
	tipo = models.PositiveIntegerField(choices=Tipo.choices, default=Tipo.Normal, verbose_name=_('tipo'))
	pendencia = models.PositiveIntegerField(choices=Pendencia.choices, default=Pendencia.Nenhuma, verbose_name=_('pendencia'))

	class Meta:
		verbose_name = _('visita')
		verbose_name_plural = _('visitas')
		ordering = ('data', 'hora', 'ciclo')