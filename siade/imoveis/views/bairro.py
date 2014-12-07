# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from siade.mixins.messages import MessageMixin
from ..models import Bairro


class BairroMixin(object):
    model = Bairro
    success_url = reverse_lazy('bairro-listar')


class Listar(BairroMixin, ListView):
    pass


class Adicionar(BairroMixin, MessageMixin, CreateView):
    success_message = u'Bairro criado com êxito'


class Detalhes(BairroMixin, DetailView):
    pass


class Editar(BairroMixin, MessageMixin, UpdateView):
    success_message = u'Bairro atualizado com êxito'


class Excluir(BairroMixin, MessageMixin, DeleteView):
    success_message = u'Bairro excluído com êxito'
