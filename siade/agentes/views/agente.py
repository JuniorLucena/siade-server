# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from siade.utils.view_urls import registry
from siade.mixins.messages import MessageMixin
from ..models import Agente


class AgenteMixin(object):
    model = Agente
    success_url = reverse_lazy('agente-listar')
    fields = ('cpf', 'nome', 'sobrenome', 'nascimento',
              'email', 'telefone', 'codigo', 'tipo', 'ativo')

    def get_context_data(self, **kwargs):
        context = super(AgenteMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model.__name__.lower()
        return context


class Listar(AgenteMixin, ListView):
    pass


class Adicionar(AgenteMixin, MessageMixin, CreateView):
    success_message = u'Agente adicionado com êxito'
    template_name = 'crud/object_form.html'


class Detalhes(AgenteMixin, DetailView):
    pass


class Editar(AgenteMixin, MessageMixin, UpdateView):
    success_message = u'Agente atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(AgenteMixin, MessageMixin, DeleteView):
    success_message = u'Agente excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'

registry.register_actions(
    'agente',
    ('listar', Listar.as_view()),
    ('adicionar', Adicionar.as_view()),
    ('detalhes', Detalhes.as_view()),
    ('editar', Editar.as_view()),
    ('excluir', Excluir.as_view())
)
urls = registry.get_urls_for_model('agente')
