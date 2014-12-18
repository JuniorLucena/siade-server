# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from siade.utils.view_urls import registry
from siade.mixins.messages import MessageMixin
from ..models import UF


class UfMixin(object):
    model = UF
    success_url = reverse_lazy('UF-listar')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UfMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model.__name__.lower()
        return context


class Listar(UfMixin, ListView):
    pass


class Adicionar(UfMixin, MessageMixin, CreateView):
    success_message = u'UF adicionado com êxito'
    template_name = 'crud/object_form.html'


class Detalhes(UfMixin, DetailView):
    pass


class Editar(UfMixin, MessageMixin, UpdateView):
    success_message = u'UF atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(UfMixin, MessageMixin, DeleteView):
    success_message = u'UF excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'

registry.register_actions(
    'uf',
    ('listar', Listar.as_view()),
    ('adicionar', Adicionar.as_view()),
    ('detalhes', Detalhes.as_view()),
    ('editar', Editar.as_view()),
    ('excluir', Excluir.as_view())
)
urls = registry.get_urls_for_model('uf')
