# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from datetime import datetime
from django.core.exceptions import NON_FIELD_ERRORS
from bootstrap3_datetime.widgets import DateTimePicker
from .models import Ciclo, Trabalho
from siade.imoveis.models import Quadra
from siade.imoveis.models import Bairro


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


class TrabalhoForm(forms.ModelForm):
    bairro = forms.ModelChoiceField(queryset=Bairro.objects.all())
    quadras = forms.RegexField(regex=r'^(\d+(-\d+)?)(,\d+(-\d+)?)*$')

    def __init__(self, agente, *args, **kwargs):
        initial = kwargs.get('initial', {})
        initial.update({'agente': agente})
        kwargs['initial'] = initial

        super(TrabalhoForm, self).__init__(*args, **kwargs)

    def clean_quadras(self):
        ranges = self.cleaned_data['quadras'].split(',')
        quadras = []
        for interval in ranges:
            item = interval.split('-')
            if len(item) > 1:
                quadras += range(int(item[0]), int(item[1])+1)
            else:
                quadras += [int(item[0])]

        return set(quadras)

    def save(self):
        ciclo = Ciclo.atual()
        agente = self.cleaned_data['agente']
        quadras = self.cleaned_data['quadras']
        bairro = self.cleaned_data['bairro']

        # Encontrar quadras já associadas
        existentes = Trabalho.objects.filter(
            quadra__bairro=bairro, quadra__numero__in=quadras, ciclo=ciclo
            ).values_list('quadra__numero', flat=True)

        quadras = quadras - set(existentes)

        # Pegar objetos quadra
        quadras_list = Quadra.objects.filter(bairro=bairro, numero__in=quadras)
        trabalhos = [Trabalho(ciclo=ciclo, agente=agente,
                              quadra=q) for q in quadras_list]
        Trabalho.objects.bulk_create(trabalhos)

        self.cleaned_data['quadras'] = quadras

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
