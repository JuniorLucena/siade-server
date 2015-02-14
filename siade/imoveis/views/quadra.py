# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, patterns
from django.db.models import ProtectedError
from django.views.generic import (CreateView, DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from extra_views import UpdateWithInlinesView
from siade.utils.fields import ReadOnlyField
from siade.mixins.messages import MessageMixin
from ..models import Quadra, Bairro, Imovel
from ..forms import LadoInline
from django.db.models import Sum

LADO_NOT_REMOVED = 'Alguns lados não podem ser removidos, pois contém imoveis.'


class QuadraMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Quadra
    permission_required = 'imoveis.can_change_quadra'
    paginate_by = 10

    def get_success_url(self):
        url = '%s:quadra:detalhes' % self.model._meta.app_label
        return reverse_lazy(url, kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(QuadraMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model
        if self.object:
            context['bairro'] = self.object.bairro
        return context


class Adicionar(QuadraMixin, MessageMixin, CreateView):
    permission_required = 'imoveis.can_add_quadra'
    success_message = u'Quadra criada com êxito'

    def get_form(self, form_class):
        id_bairro = self.kwargs.get('bairro')
        self.bairro = Bairro.objects.get(pk=id_bairro)

        form_kwargs = self.get_form_kwargs()
        form = form_class(**form_kwargs)
        form.fields['bairro'] = ReadOnlyField(initial=self.bairro)

        return form

    def get_context_data(self, **kwargs):
        context = super(Adicionar, self).get_context_data(**kwargs)
        context['bairro'] = getattr(self, 'bairro', None)
        return context


class Detalhes(QuadraMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super(Detalhes, self).get_context_data(**kwargs)
        lados = self.object.lados.all()
        num_lado = self.kwargs.get('lado')
        if lados.count() > 0:
            if num_lado:
                lado = self.object.lados.get(numero=num_lado)
            else:
                lado = self.object.lados.first()
            imoveis = Imovel.objects.filter(lado=lado)
            context['imovel_list'] = imoveis
            context['lado'] = lado

            quadras = Quadra.objects.filter(lados=lado)
            quadras = quadras.annotate(
                habitantes=Sum('lados__imoveis__habitantes'),
                caes=Sum('lados__imoveis__caes'),
                gatos=Sum('lados__imoveis__gatos'))
            context['quadras'] = quadras

        context['lado_list'] = lados
        return context


class Editar(QuadraMixin, MessageMixin, UpdateWithInlinesView):
    success_message = u'Quadra atualizado com êxito'
    inlines = [LadoInline]

    def forms_valid(self, form, inlines):
        try:
            super(Editar, self).forms_valid(form, inlines)
        except ProtectedError:
            messages.warning(self.request, LADO_NOT_REMOVED)
        return HttpResponseRedirect(self.get_success_url())


class Excluir(QuadraMixin, MessageMixin, DeleteView):
    permission_required = 'imoveis.can_delete_quadra'
    success_message = u'Quadra excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('imoveis:bairro:detalhes',
                            kwargs={'pk': self.object.bairro})

urls = patterns(
    '',
    url(r'^adicionar/(?P<bairro>\d+)/$', Adicionar.as_view(),
        name='adicionar'),
    url(r'^(?P<pk>\d+)/$', Detalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>\d+)/(?P<lado>\d+)/$', Detalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>\d+)/editar$', Editar.as_view(), name='editar'),
    url(r'^(?P<pk>\d+)/excluir$', Excluir.as_view(), name='excluir')
)
