# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.db.models import Max
from .models import Ciclo, Trabalho
from siade.imoveis.models import Quadra
from ajax_filtered_fields.forms.fields import ManyToManyByRelatedField


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
    quadras = ManyToManyByRelatedField(Quadra, 'bairro', allow_all=False)

    def save(self):
        ciclo = Ciclo.atual()
        agente = self.cleaned_data['agente']
        quadras = []
        for quadra in self.cleaned_data['quadras']:
            quadras += [Trabalho(ciclo=ciclo, agente=agente, quadra=quadra)]
        Trabalho.objects.bulk_create(quadras)

    class Meta:
        model = Trabalho
        exclude = ('ciclo', 'quadra')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together':
                "Já existe %(model_name)s para este %(field_labels)s",
            }
        }

    def _get_validation_exclusions(self):
        exclude = super(TrabalhoForm, self)._get_validation_exclusions()
        exclude.remove('ciclo')
        return exclude
