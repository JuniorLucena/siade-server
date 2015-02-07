# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import defaultdict
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.db import IntegrityError
from django.db.models import Q
from django.utils.html import format_html
from .models import Ciclo, Trabalho
from siade.imoveis.models import Quadra


class IniciarCicloForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super(IniciarCicloForm, self).save(False)
        atual = Ciclo.atual()
        if instance.ano_base == atual.ano_base:
            instance.numero = atual.numero + 1
        else:
            instance.numero = 1

        if commit:
            instance.save()
        return

    class Meta:
        model = Ciclo
        exclude = ('fechado_em', 'numero')


class TrabalhoForm(forms.ModelForm):
    quadras = forms.MultipleChoiceField(
        required=False, widget=forms.CheckboxSelectMultiple())

    def __init__(self, agente, *args, **kwargs):
        # Popular valores do formulário
        self.trabalhos = Trabalho.objects.filter(ciclo=Ciclo.atual())
        initial = kwargs.get('initial', {})
        initial.update({
            'quadras': self.trabalhos.filter(agente=agente)
                           .values_list('quadra', flat=True),
            'agente': agente
        })
        kwargs['initial'] = initial

        super(TrabalhoForm, self).__init__(*args, **kwargs)

        # Popular opções de quadras quadras
        exclude = self.trabalhos.filter(~Q(agente=agente))\
                                .values_list('quadra', flat=True)
        quadras = defaultdict(list)
        for q in Quadra.objects.order_by('bairro', 'numero')\
                       .exclude(id__in=exclude)\
                       .values('bairro__nome', 'id', 'numero'):
            quadras[q['bairro__nome']] += [(q['id'], q['numero'])]
        self.fields['quadras'].choices = quadras.items()

    def save(self):
        ciclo = Ciclo.atual()
        agente = self.cleaned_data['agente']
        quadras = self.cleaned_data['quadras']
        self.trabalhos.filter(agente=agente).filter(
            ~Q(quadra__in=quadras)).delete()
        for quadra in quadras:
            q = Quadra(pk=quadra)
            trabalho = Trabalho(ciclo=ciclo, agente=agente, quadra=q)
            try:
                trabalho.save()
            except IntegrityError:
                pass

    class Meta:
        model = Trabalho
        exclude = ('ciclo', 'quadra')
        widgets = {'agente': forms.HiddenInput()}
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together':
                "Já existe %(model_name)s para este %(field_labels)s",
            }
        }
