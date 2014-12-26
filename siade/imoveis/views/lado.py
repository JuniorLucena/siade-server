# -*- coding: utf-8 -*-
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.utils.fields import ReadOnlyField
from siade.mixins.messages import MessageMixin
from ..models import LadoQuadra, Quadra


class LadoMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'imoveis.can_change_quadra'
    success_message = u'Quadra atualizada com êxito'
    model = LadoQuadra

    def get_success_url(self):
        app_label = self.model._meta.app_label
        return reverse_lazy('%s:quadra:detalhes' % app_label,
                            kwargs={'lado': self.object.quadra.numero,
                                    'pk': self.quadra.id})

    def get_context_data(self, **kwargs):
        context = super(LadoMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model
        return context


class Adicionar(LadoMixin, MessageMixin, CreateView):
    def get_form(self, form_class):
        id_quadra = self.kwargs.get('quadra')
        self.quadra = Quadra.objects.get(pk=id_quadra)

        form_kwargs = self.get_form_kwargs()
        form = form_class(**form_kwargs)
        form.fields['quadra'] = ReadOnlyField(initial=self.quadra)

        return form

    def get_context_data(self, **kwargs):
        context = super(Adicionar, self).get_context_data(**kwargs)
        context['bairro'] = getattr(self, 'bairro', None)
        return context


class Editar(LadoMixin, MessageMixin, UpdateView):
    def get_form(self, form_class):
        form_kwargs = self.get_form_kwargs()
        form = form_class(**form_kwargs)
        form.fields['quadra'] = ReadOnlyField(initial=self.object.quadra)
        return form


class Excluir(LadoMixin, MessageMixin, DeleteView):
    template_name = 'crud/object_confirm_delete.html'

from django.conf.urls import url, patterns
urls = patterns(
    '',
    url(r'^adicionar/(?P<quadra>\d+)/$', Adicionar.as_view(),
        name='adicionar'),
    url(r'^(?P<pk>\d+)/editar$', Editar.as_view(), name='editar'),
    url(r'^(?P<pk>\d+)/excluir$', Excluir.as_view(), name='excluir')
)
