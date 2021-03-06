# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, patterns
from django.db.models import ProtectedError, Sum
from django.views.generic import DeleteView, DetailView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from siade.mixins.messages import MessageMixin
from ..models import Quadra, Bairro, Imovel
from ..forms import LadoInline, QuadraForm

LADO_NOT_REMOVED = 'Alguns lados não podem ser removidos, pois contém imoveis.'


class QuadraMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Quadra
    form_class = QuadraForm
    permission_required = 'imoveis.change_quadra'
    raise_exception = True
    paginate_by = 50

    def get_success_url(self):
        nextUrl = self.request.GET.get('next')
        if nextUrl is None:
            app_label = self.model._meta.app_label
            nextUrl = reverse('%s:quadra:detalhes' % app_label,
                              kwargs={'pk': self.object.id})
        return nextUrl

    def get_context_data(self, **kwargs):
        context = super(QuadraMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model
        if self.object:
            context['bairro'] = self.object.bairro
        return context


class Adicionar(QuadraMixin, MessageMixin, CreateWithInlinesView):
    permission_required = 'imoveis.add_quadra'
    success_message = 'Quadra criada com êxito'
    inlines = [LadoInline]

    def get_form_kwargs(self):
        id_bairro = self.kwargs.get('bairro')
        self.bairro = Bairro.objects.get(pk=id_bairro)

        form_kwargs = super(Adicionar, self).get_form_kwargs()
        form_kwargs.update({'initial': {'bairro': self.bairro}})
        return form_kwargs

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
    success_message = 'Quadra atualizado com êxito'
    inlines = [LadoInline]

    def get_form_kwargs(self):
        kwargs = super(Editar, self).get_form_kwargs()
        kwargs.update({'initial': {'bairro': self.object.bairro}})
        return kwargs

    def forms_valid(self, form, inlines):
        try:
            super(Editar, self).forms_valid(form, inlines)
        except ProtectedError:
            messages.warning(self.request, LADO_NOT_REMOVED)
        return HttpResponseRedirect(self.get_success_url())


class Excluir(QuadraMixin, MessageMixin, DeleteView):
    permission_required = 'imoveis.delete_quadra'
    success_message = 'Quadra excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'

    def get_success_url(self):
        return reverse('imoveis:bairro:detalhes',
                       kwargs={'pk': self.object.bairro.id})

urls = patterns(
    '',
    url(r'^adicionar/(?P<bairro>[^/]+)/$', Adicionar.as_view(),
        name='adicionar'),
    url(r'^(?P<pk>[^/]+)/$', Detalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>[^/]+)/(?P<lado>\w+)/$', Detalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>[^/]+)/editar$', Editar.as_view(), name='editar'),
    url(r'^(?P<pk>[^/]+)/excluir$', Excluir.as_view(), name='excluir')
)
