from django.forms import ModelForm
from .models import Agente


class AgenteForm(ModelForm):
    fields = ('cpf', 'nome', 'sobrenome', 'data_nascimento',
              'email', 'telefone', 'codigo', 'tipo')
    model = Agente
