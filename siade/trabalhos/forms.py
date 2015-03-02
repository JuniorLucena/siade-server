# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django import forms
from datetime import datetime
from bootstrap3_datetime.widgets import DateTimePicker
from .models import Ciclo, Trabalho
from siade.imoveis.models import Quadra


def CicloDatePicker():
    return DateTimePicker(options={
        'format': 'DD/MM/YYYY', 'pickTime': False,
        'startDate': str(datetime.now())
    })


class IniciarCicloForm(forms.ModelForm):
    data_inicio = forms.DateField(widget=CicloDatePicker())
    data_fim = forms.DateField(widget=CicloDatePicker())

    def save(self, commit=True):
        instance = super(IniciarCicloForm, self).save(False)
        atual = Ciclo.atual()
        if atual is not None and instance.ano_base == atual.ano_base:
            instance.numero = atual.numero + 1
        else:
            instance.numero = 1

        if commit:
            instance.save()
        return

    class Meta:
        model = Ciclo
        exclude = ('fechado_em', 'numero')


class TrabalhoForm(forms.Form):
    quadras = forms.MultipleChoiceField(
        required=False, widget=forms.MultipleHiddenInput())

    def __init__(self, agente, *args, **kwargs):
        self.trabalhos = Trabalho.objects.filter(ciclo=Ciclo.atual())
        self.agente = agente

        # atualizar valores iniciais
        initial = kwargs.get('initial', {})
        initial.update({
            'quadras': self.trabalhos.filter(agente=agente)\
                           .values_list('quadra', flat=True),
        })
        kwargs['initial'] = initial

        super(TrabalhoForm, self).__init__(*args, **kwargs)

        # Quadras e não estão associada a esse a agente ou a nenhum a agente
        trabalhos = self.trabalhos.exclude(agente=agente)\
                        .values_list('quadra__id', flat=True)
        quadras = Quadra.objects.exclude(id__in=trabalhos).values_list('id', 'numero')
        self.fields['quadras'].choices = quadras

    def save(self):
        ciclo = Ciclo.atual()
        quadras = self.cleaned_data['quadras']
        # Apagar trabalhos do agente que foram removidos
        self.trabalhos.filter(~Q(quadra__in=quadras),
                              agente=self.agente).delete()
        # Pegar trabalhos já existentes
        existentes = self.trabalhos.filter(quadra__in=quadras)\
                         .values_list('quadra', flat=True)
        # Remover da lista de quadras
        quadras = set(quadras) - set(existentes)
        # Criar trabalhos novos
        trabalhos = [Trabalho(ciclo=ciclo, agente=self.agente,
                              quadra=Quadra(q)) for q in quadras]
        Trabalho.objects.bulk_create(trabalhos)
