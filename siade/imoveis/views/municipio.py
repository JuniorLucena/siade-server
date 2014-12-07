# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from siade.mixins.messages import MessageMixin
from ..models import Municipio


class MunicipioView(object):
    model = Municipio
    success_url = reverse_lazy('Municipio-listar')


class MunicipioListar(MunicipioView, ListView):
    pass


class MunicipioAdicionar(MunicipioView, MessageMixin, CreateView):
    pass


class MunicipioEditar(MunicipioView, MessageMixin, UpdateView):
    success_message = u'Municipio atualizado com êxito'


class MunicipioApagar(MunicipioView, MessageMixin, DeleteView):
    success_message = u'Municipio excluído com êxito'
