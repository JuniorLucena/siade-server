# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, patterns
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.mixins.messages import MessageMixin
from ..models import Municipio


class MunicipioMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Municipio
    permission_required = 'imoveis.change_municipio'
    raise_exception = True
    paginate_by = 50
    success_url = reverse_lazy('%s:municipio:listar' % model._meta.app_label)

    def get_context_data(self, **kwargs):
        context = super(MunicipioMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model
        return context


class Listar(MunicipioMixin, ListView):
    pass


class Adicionar(MunicipioMixin, MessageMixin, CreateView):
    success_message = 'Municipio adicionado com êxito'
    template_name = 'crud/object_form.html'


class Detalhes(MunicipioMixin, DetailView):
    pass


class Editar(MunicipioMixin, MessageMixin, UpdateView):
    success_message = 'Municipio atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(MunicipioMixin, MessageMixin, DeleteView):
    permission_required = 'imoveis.delete_municipio'
    success_message = 'Municipio excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'


urls = patterns(
    '',
    url(r'^$', Listar.as_view(), name='listar'),
    url(r'^adicionar/$', Adicionar.as_view(), name='adicionar'),
    url(r'^(?P<pk>[^/]+)/$', Detalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>[^/]+)/editar$', Editar.as_view(), name='editar'),
    url(r'^(?P<pk>[^/]+)/excluir$', Excluir.as_view(), name='excluir')
)
