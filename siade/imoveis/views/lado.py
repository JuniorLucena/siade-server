# -*- coding: utf-8 -*-
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from siade.utils.view_urls import registry
from siade.utils.fields import ReadOnlyField
from siade.mixins.messages import MessageMixin
from ..models import LadoQuadra, Quadra


class LadoMixin(object):
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
    success_message = u'Lado criado com êxito'

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
    success_message = u'Lado atualizado com êxito'

    def get_form(self, form_class):
        form_kwargs = self.get_form_kwargs()
        form = form_class(**form_kwargs)
        form.fields['quadra'] = ReadOnlyField(initial=self.object.quadra)

        return form


class Excluir(LadoMixin, MessageMixin, DeleteView):
    success_message = u'Lado excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'


registry.register_actions(
    'ladoquadra',
    ('adicionar', Adicionar.as_view(),
        r'^adicionar/(?P<quadra>\d+)/$'),
    ('editar', Editar.as_view()),
    ('excluir', Excluir.as_view())
)
urls = registry.get_urls_for_model('ladoquadra')
