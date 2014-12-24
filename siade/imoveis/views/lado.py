# -*- coding: utf-8 -*-
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.utils.view_urls import registry
from siade.utils.fields import ReadOnlyField
from siade.mixins.messages import MessageMixin
from ..models import LadoQuadra, Quadra


class LadoMixin(LoginRequiredMixin, PermissionRequiredMixin):
    success_message = u'Quadra atualizada com êxito'
    model = LadoQuadra

    def get_success_url(self):
        return reverse_lazy('quadra-detalhes', kwargs={
            'pk': self.quadra.id,
            'lado': self.object.quadra.numero
        })

    def get_context_data(self, **kwargs):
        context = super(LadoMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model.__name__.lower()
        return context


class Adicionar(LadoMixin, MessageMixin, CreateView):
    permission_required = 'imoveis.change_quadra'

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
    permission_required = 'imoveis.change_quadra'

    def get_form(self, form_class):
        form_kwargs = self.get_form_kwargs()
        form = form_class(**form_kwargs)
        form.fields['quadra'] = ReadOnlyField(initial=self.object.quadra)

        return form


class Excluir(LadoMixin, MessageMixin, DeleteView):
    template_name = 'crud/object_confirm_delete.html'
    permission_required = 'imoveis.change_quadra'


registry.register_actions(
    'ladoquadra',
    ('adicionar', Adicionar.as_view(),
        r'^adicionar/(?P<quadra>\d+)/$'),
    ('editar', Editar.as_view()),
    ('excluir', Excluir.as_view())
)
urls = registry.get_urls_for_model('ladoquadra')
