# -*- coding: utf-8 -*
from __future__ import unicode_literals
from django.conf.urls import url, patterns
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum, Count
from django.forms.models import modelform_factory
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.mixins.messages import MessageMixin
from ..models import Bairro
from ..forms import BairroForm


class BairroMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Bairro
    form_class = BairroForm
    success_url = reverse_lazy('%s:bairro:listar' % model._meta.app_label)
    permission_required = 'imoveis.change_bairro'
    raise_exception = True
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super(BairroMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model
        return context


class Listar(BairroMixin, ListView):
    pass


class Adicionar(BairroMixin, MessageMixin, CreateView):
    success_message = 'Bairro criado com êxito'
    template_name = 'crud/object_form.html'
    permission_required = 'imoveis.add_bairro'

    def get_form_class(self):
        if self.request.user.is_staff:
            return modelform_factory(self.model)
        else:
            return super(Adicionar, self).get_form_class()

    def get_form_kwargs(self):
        kwargs = super(Adicionar, self).get_form_kwargs()
        agente = self.request.user
        kwargs.update({'initial': {'municipio': agente.municipio}})
        return kwargs


class Detalhes(BairroMixin, DetailView):
    def get_context_data(self, **kwargs):
        quadras = self.object.quadras.all()
        quadras = quadras.annotate(total_imoveis=Count('lados__imoveis'))
        quadras = quadras.annotate(total_caes=Sum('lados__imoveis__caes'))
        quadras = quadras.annotate(total_gatos=Sum('lados__imoveis__gatos'))

        context = super(Detalhes, self).get_context_data(**kwargs)
        context.update({
            'quadra_list': quadras,
        })
        return context


class Editar(BairroMixin, MessageMixin, UpdateView):
    success_message = 'Bairro atualizado com êxito'
    template_name = 'crud/object_form.html'

    def get_form_kwargs(self):
        kwargs = super(Editar, self).get_form_kwargs()
        kwargs.update({'initial': {'municipio': self.object.municipio}})
        return kwargs


class Excluir(BairroMixin, MessageMixin, DeleteView):
    success_message = 'Bairro excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'
    permission_required = 'imoveis.delete_bairro'


urls = patterns(
    '',
    url(r'^$', Listar.as_view(), name='listar'),
    url(r'^adicionar/$', Adicionar.as_view(), name='adicionar'),
    url(r'^(?P<pk>[^/]+)/$', Detalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>[^/]+)/editar$', Editar.as_view(), name='editar'),
    url(r'^(?P<pk>[^/]+)/excluir$', Excluir.as_view(), name='excluir')
)
