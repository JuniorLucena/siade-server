import re
from django import forms
from django.utils.encoding import smart_text
from localflavor.br.forms import BRPhoneNumberField, BRCPFField
from input_mask.contrib.localflavor.br.widgets import (BRPhoneNumberInput,
                                                       BRCPFInput)
from .models import Agente


class AgenteForm(forms.ModelForm):
    cpf = BRCPFField(widget=BRCPFInput, label='CPF')
    telefone = BRPhoneNumberField(widget=BRPhoneNumberInput, required=False)

    def clean_cpf(self):
        value = self.cleaned_data['cpf']
        if not value.isdigit():
            value = re.sub("[-\. ]", "", value)
        return int(value)

    def clean_telefone(self):
        value = self.cleaned_data['telefone']
        value = re.sub('-', '', smart_text(value))
        if value == '':
            return None
        else:
            return int(value)

    class Meta:
        model = Agente
        fields = ('cpf', 'nome', 'sobrenome', 'nascimento',
                  'email', 'telefone', 'codigo', 'tipo','municipio')
