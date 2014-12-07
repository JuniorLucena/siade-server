# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from siade.mixins.messages import MessageMixin
from ..models import Agente


class AgenteMixin(object):
    model = Agente
    success_url = reverse_lazy('agente-listar')
    fields = ('cpf', 'nome', 'sobrenome', 'nascimento',
              'email', 'telefone', 'codigo', 'tipo', 'ativo')


class listar(AgenteMixin, ListView):
    pass


class adicionar(AgenteMixin, MessageMixin, CreateView):
    success_message = u'Agente adicionado com êxito'


class detalhes(AgenteMixin, DetailView):
    pass


class editar(AgenteMixin, MessageMixin, UpdateView):
    success_message = u'Agente atualizado com êxito'


class excluir(AgenteMixin, MessageMixin, DeleteView):
    success_message = u'Agente excluído com êxito'
