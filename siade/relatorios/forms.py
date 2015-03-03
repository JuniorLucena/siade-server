from datetime import datetime
from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from siade.agentes.models import Agente
from siade.trabalhos.models import Ciclo
from bootstrap3_datetime.widgets import DateTimePicker


def DatePicker():
    options = {'format': 'DD/MM/YYYY', 'pickTime': False}
    return DateTimePicker(options=options)


class D1Form(forms.Form):
    data = forms.DateField(widget=DatePicker())
    agentes = forms.MultipleChoiceField(
        required=False, widget=CheckboxSelectMultiple(),
        choices=Agente.objects.values_list('id', 'nome').filter(
            tipo=Agente.Tipo.AgenteCampo))

    def clean_data(self):
        data = self.cleaned_data["data"]
        ciclo = Ciclo.atual()
        if data >= ciclo.data_inicio and data <= ciclo.data_fim:
            return data
        else:
            raise forms.ValidationError("Data fora do ciclo")


class D7Form(forms.Form):
    semana = forms.IntegerField(initial=1, min_value=1)
    agentes = forms.MultipleChoiceField(
        required=False, widget=CheckboxSelectMultiple(),
        choices=Agente.objects.values_list('id', 'nome').filter(
            tipo=Agente.Tipo.AgenteCampo))

    def clean_semana(self):
        semana = self.cleaned_data['semana']
        ciclo = Ciclo.atual()
        data_inicio = ciclo.data_inicio + timedelta(days=(semana-1)*7)
        data_fim = ciclo.data_inicio + timedelta(days=semana*7)
        print data_inicio, data_fim
        if data_inicio > ciclo.data_fim or data_fim > ciclo.data_fim:
            raise forms.ValidationError("Semana fora do ciclo.")
        else:
            return semana
