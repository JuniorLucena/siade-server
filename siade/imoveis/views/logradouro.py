# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from siade.mixins.messages import MessageMixin
from ..models import Logradouro


class LogradouroMixin(object):
    model = Logradouro
    success_url = reverse_lazy('Logradouro-listar')
    paginate_by = 5


class Listar(LogradouroMixin, ListView):
    pass


class Adicionar(LogradouroMixin, MessageMixin, CreateView):
    pass


class Detalhes(LogradouroMixin, DetailView):
    pass


class Editar(LogradouroMixin, MessageMixin, UpdateView):
    success_message = u'Logradouro atualizado com êxito'


class Excluir(LogradouroMixin, MessageMixin, DeleteView):
    success_message = u'Logradouro excluído com êxito'
