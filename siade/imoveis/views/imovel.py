# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.utils.fields import ReadOnlyField
from siade.mixins.messages import MessageMixin
from ..models import Imovel, LadoQuadra
from ..forms import ImovelForm


class ImovelMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Imovel
    permission_required = 'imoveis.change_imovel'
    raise_exception = True
    paginate_by = 50

    def get_success_url(self):
        nextUrl = self.request.GET.get('next')
        if nextUrl is None:
            app_label = self.model._meta.app_label
            nextUrl = reverse('%s:imovel:detalhes' % app_label,
                              kwargs={'pk': self.object.id})
        return nextUrl

    def get_context_data(self, **kwargs):
        context = super(ImovelMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model
        if self.object:
            context['quadra'] = self.object.lado.quadra
            context['bairro'] = context['quadra'].bairro
        return context


class Adicionar(ImovelMixin, MessageMixin, CreateView):
    success_message = u'Imovel criado com êxito'

    def get_form(self, form_class):
        lado = self.kwargs.get('lado')
        quadra = self.kwargs.get('quadra')
        self.lado = LadoQuadra.objects.get(numero=lado, quadra=quadra)

        form_kwargs = self.get_form_kwargs()
        form_kwargs.update({'initial': {'lado': self.lado}})

        form = form_class(**form_kwargs)
        form.fields['lado'] = ReadOnlyField()

        return form

    def get_context_data(self, **kwargs):
        context = super(Adicionar, self).get_context_data(**kwargs)
        lado = getattr(self, 'lado', None)
        context['lado'] = lado
        if lado:
            context.update({
                'quadra': lado.quadra,
                'bairro': lado.quadra.bairro
            })
        return context


class Detalhes(ImovelMixin, DetailView):
    def get_context_data(self, **kwargs):
        context = super(Detalhes, self).get_context_data(**kwargs)
        context['lado'] = self.object.lado
        context['quadra'] = self.object.lado.quadra
        return context


class Editar(ImovelMixin, MessageMixin, UpdateView):
    success_message = u'Imovel atualizado com êxito'
    form_class = ImovelForm

    def get_form(self, form_class):
        form = super(Editar, self).get_form(form_class)
        return form

    def get_form_kwargs(self):
        kwargs = super(Editar, self).get_form_kwargs()
        kwargs.update({'initial': {'lado': self.object.lado}})
        return kwargs


class Excluir(ImovelMixin, MessageMixin, DeleteView):
    permission_required = 'imoveis.delete_imovel'
    success_message = u'Imovel excluído com êxito'

    def get_success_url(self):
        app_label = self.model._meta.app_label
        return reverse('%s:quadra:detalhes' % app_label, kwargs={
            'lado': self.object.lado.id,
            'pk': self.object.lado.quadra.id
        })


urls = patterns(
    '',
    url(r'^adicionar/(?P<quadra>[^/]+)/(?P<lado>\w+)/?$', Adicionar.as_view(),
        name='adicionar'),
    url(r'^(?P<pk>[^/]+)/$', Detalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>[^/]+)/editar$', Editar.as_view(), name='editar'),
    url(r'^(?P<pk>[^/]+)/excluir$', Excluir.as_view(), name='excluir')
)
