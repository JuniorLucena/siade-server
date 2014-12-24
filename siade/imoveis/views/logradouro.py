# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.utils.view_urls import registry
from siade.mixins.messages import MessageMixin
from ..models import Logradouro


class LogradouroMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Logradouro
    success_url = reverse_lazy('logradouro-listar')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(LogradouroMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model.__name__.lower()
        return context


class Listar(LogradouroMixin, ListView):
    permission_required = "imoveis.view_logradouro"


class Adicionar(LogradouroMixin, MessageMixin, CreateView):
    permission_required = "imoveis.add_logradouro"
    template_name = 'crud/object_form.html'


class Detalhes(LogradouroMixin, DetailView):
    permission_required = "imoveis.view_logradouro"


class Editar(LogradouroMixin, MessageMixin, UpdateView):
    permission_required = "imoveis.change_logradouro"
    success_message = u'Logradouro atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(LogradouroMixin, MessageMixin, DeleteView):
    permission_required = "imoveis.delete_logradouro"
    success_message = u'Logradouro excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'

registry.register_actions(
    'logradouro',
    ('listar', Listar.as_view()),
    ('adicionar', Adicionar.as_view()),
    ('detalhes', Detalhes.as_view()),
    ('editar', Editar.as_view()),
    ('excluir', Excluir.as_view())
)
urls = registry.get_urls_for_model('logradouro')
