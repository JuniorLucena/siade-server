from django import forms
from siade.utils.fields import ReadOnlyField
from .models import Imovel


class ImovelForm(forms.ModelForm):
    lado = ReadOnlyField()

    class Meta:
        model = Imovel
        exclude = []
