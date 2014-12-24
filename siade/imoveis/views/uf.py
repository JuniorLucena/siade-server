# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.utils.view_urls import registry
from siade.mixins.messages import MessageMixin
from ..models import UF


class UfMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = UF
    success_url = reverse_lazy('UF-listar')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UfMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model.__name__.lower()
        return context


class Listar(UfMixin, ListView):
    permission_required = 'imoveis.view_uf'


class Adicionar(UfMixin, MessageMixin, CreateView):
    permission_required = 'imoveis.add_uf'
    success_message = u'UF adicionado com êxito'
    template_name = 'crud/object_form.html'


class Detalhes(UfMixin, DetailView):
    permission_required = 'imoveis.view_uf'


class Editar(UfMixin, MessageMixin, UpdateView):
    permission_required = 'imoveis.change_uf'
    success_message = u'UF atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(UfMixin, MessageMixin, DeleteView):
    permission_required = 'imoveis.delete_uf'
    success_message = u'UF excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'

registry.register_actions(
    'uf',
    ('listar', Listar.as_view()),
    ('adicionar', Adicionar.as_view()),
    ('detalhes', Detalhes.as_view()),
    ('editar', Editar.as_view()),
    ('excluir', Excluir.as_view())
)
urls = registry.get_urls_for_model('uf')
