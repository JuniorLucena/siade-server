import re
from django import forms
from django.utils.encoding import smart_text
from django.forms.widgets import CheckboxSelectMultiple
from localflavor.br.forms import BRPhoneNumberField, BRCPFField
from input_mask.contrib.localflavor.br.widgets import (BRPhoneNumberInput,
                                                       BRCPFInput)
from siade.agentes.models import Agente
from siade.trabalhos.models import Ciclo
from bootstrap3_datetime.widgets import DateTimePicker


class D1Form(forms.Form):
	data = forms.DateField(widget=DateTimePicker(options={"format": "DD/MM/YYYY",
                                       "pickTime": False}))
	agentes = forms.MultipleChoiceField(required=False, widget=CheckboxSelectMultiple(),
									    choices=Agente.objects.values_list('id', 'nome').filter(tipo=Agente.Tipo.AgenteCampo))

	def clean_data(self):
		data = self.cleaned_data["data"]
		ciclo = Ciclo.atual()
		if data >= ciclo.data_inicio and data <= ciclo.data_fim:
			return data
		else: 
			raise forms.ValidationError("Data fora do Cilclo")
	



	