from django import forms
from extra_views import InlineFormSet
from siade.utils.fields import ReadOnlyField
from .models import Imovel, LadoQuadra


class LadoInline(InlineFormSet):
    model = LadoQuadra


class ImovelForm(forms.ModelForm):
    lado = ReadOnlyField()

    class Meta:
        model = Imovel
        exclude = []

    