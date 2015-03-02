# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, patterns
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.mixins.messages import MessageMixin
from ..models import UF


class UfMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = UF
    permission_required = 'imoveis.change_uf'
    raise_exception = True
    paginate_by = 50
    success_url = reverse_lazy('%s:uf:listar' % model._meta.app_label)

    def get_context_data(self, **kwargs):
        context = super(UfMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model
        return context


class Listar(UfMixin, ListView):
    pass


class Adicionar(UfMixin, MessageMixin, CreateView):
    success_message = 'UF adicionado com êxito'
    template_name = 'crud/object_form.html'


class Detalhes(UfMixin, DetailView):
    pass


class Editar(UfMixin, MessageMixin, UpdateView):
    success_message = 'UF atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(UfMixin, MessageMixin, DeleteView):
    permission_required = 'imoveis.delete_uf'
    success_message = 'UF excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'


urls = patterns(
    '',
    url(r'^$', Listar.as_view(), name='listar'),
    url(r'^adicionar/$', Adicionar.as_view(), name='adicionar'),
    url(r'^(?P<pk>[^/]+)/$', Detalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>[^/]+)/editar$', Editar.as_view(), name='editar'),
    url(r'^(?P<pk>[^/]+)/excluir$', Excluir.as_view(), name='excluir')
)
