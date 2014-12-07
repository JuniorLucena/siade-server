# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from siade.mixins.messages import MessageMixin
from ..models import UF


class UFView(object):
    model = UF
    success_url = reverse_lazy('UF-listar')


class UFListar(UFView, ListView):
    pass


class UFAdicionar(UFView, MessageMixin, CreateView):
    pass


class UFEditar(UFView, MessageMixin, UpdateView):
    success_message = u'UF atualizado com êxito'


class UFApagar(UFView, MessageMixin, DeleteView):
    success_message = u'UF excluído com êxito'
