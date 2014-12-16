# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from siade.utils.fields import ReadOnlyField
from siade.utils.view_urls import registry
from siade.mixins.messages import MessageMixin
from ..models import Imovel, Quadra, LadoQuadra
from ..forms import ImovelForm


class ImovelMixin(object):
    model = Imovel

    def get_context_data(self, **kwargs):
        context = super(ImovelMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model.__name__.lower()
        return context


class Adicionar(ImovelMixin, MessageMixin, CreateView):
    success_message = u'Imovel criado com êxito'

    def get_form(self, form_class):
        id_lado = self.kwargs.get('lado')
        self.lado = LadoQuadra.objects.get(pk=id_lado)

        form_kwargs = self.get_form_kwargs()
        form_kwargs.update({'initial': {'lado': self.lado}})

        form = form_class(**form_kwargs)
        form.fields['lado'] = ReadOnlyField()

        return form

    def get_success_url(self):
        return reverse_lazy('imovel-detalhes', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(Adicionar, self).get_context_data(**kwargs)
        context['lado'] = getattr(self, 'lado', None)
        return context


class Detalhes(ImovelMixin, DetailView):
    pass


class Editar(ImovelMixin, MessageMixin, UpdateView):
    success_message = u'Imovel atualizado com êxito'
    form_class = ImovelForm

    def get_form(self, form_class):
        form = super(Editar, self).get_form(form_class)
        print '-- lado ', form.fields['lado'].initial,
        return form

    def get_form_kwargs(self):
        kwargs = super(Editar, self).get_form_kwargs()
        kwargs.update({'initial': {'lado': self.object.lado}})
        return kwargs

    def get_success_url(self):
        return reverse_lazy('imovel-detalhes', kwargs={'pk': self.object.id})


class Excluir(ImovelMixin, MessageMixin, DeleteView):
    success_message = u'Imovel excluído com êxito'

    def get_success_url(self):
        return reverse_lazy('quadra-detalhes', kwargs={
            'lado': self.object.lado.id,
            'pk': self.object.lado.quadra.id
        })


registry.register_actions(
    'imovel',
    ('adicionar', Adicionar.as_view(),
        r'^adicionar/(?P<quadra>\d+)/(?P<lado>\d+)/?$'),
    ('detalhes', Detalhes.as_view()),
    ('editar', Editar.as_view()),
    ('excluir', Excluir.as_view())
)
urls = registry.get_urls_for_model('imovel')
