from django import forms
from extra_views import InlineFormSet
from siade.utils.fields import ReadOnlyField
from .models import Imovel, LadoQuadra, Quadra, Bairro


class LadoInline(InlineFormSet):
    model = LadoQuadra


class ImovelForm(forms.ModelForm):
    lado = ReadOnlyField()

    class Meta:
        model = Imovel
        exclude = []


class QuadraForm(forms.ModelForm):
    bairro = ReadOnlyField()

    class Meta:
        model = Quadra
        exclude = []


class BairroForm(forms.ModelForm):
    municipio = ReadOnlyField()

    class Meta:
        model = Bairro
        exclude = []