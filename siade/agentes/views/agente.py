# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.mixins.messages import MessageMixin
from ..models import Agente


class AgenteMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Agente
    fields = ('cpf', 'nome', 'sobrenome', 'nascimento',
              'email', 'telefone', 'codigo', 'tipo')
    form_class = modelform_factory(Agente, fields=fields)
    permission_required = 'agentes.change_agente'

    def get_success_url(self):
        nextUrl = self.request.GET.get('next')
        if nextUrl is None:
            app_label = self.model._meta.app_label
            nextUrl = reverse('%s:agente:detalhes' % app_label,
                              kwargs={'pk': self.object.id})
        return nextUrl

    def get_context_data(self, **kwargs):
        context = super(AgenteMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model
        context['fields'] = getattr(self, 'fields',
                                    self.model._meta.get_all_field_names())
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

from django.conf.urls import url, patterns
urls = patterns(
    '',
    url(r'^$', Listar.as_view(), name='listar'),
    url(r'^adicionar/$', Adicionar.as_view(), name='adicionar'),
    url(r'^(?P<pk>\d+)/$', Detalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>\d+)/editar$', Editar.as_view(), name='editar'),
    url(r'^(?P<pk>\d+)/excluir$', Excluir.as_view(), name='excluir')
)
