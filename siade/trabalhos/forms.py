from django import forms
from django.db.models import Max
from .models import Ciclo, Trabalho


class IniciarCicloForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super(IniciarCicloForm, self).save(False)
        ultimo = Ciclo.objects.filter(ano_base=instance.ano_base)\
                              .aggregate(max=Max('numero'))['max']
        instance.numero = 1 if ultimo is None else ultimo + 1
        if(commit):
            instance.save()
        return

    class Meta:
        model = Ciclo
        exclude = ('fechado_em', 'numero')


class TrabalhoForm(forms.ModelForm):
    class Meta:
        model = Trabalho
        exclude = ('ciclo',)
        widgets = {
            'agente': forms.RadioSelect(),
            'quadra': forms.RadioSelect()
        }
