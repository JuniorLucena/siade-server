# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from siade.mixins.messages import MessageMixin
from ..models import UF


class ContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ContextMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()

        object_urls = {}
        for n in ('listar', 'adicionar', 'detalhes', 'editar', 'excluir'):
            object_urls[n] = 'uf-%s' % n

        context['object_urls'] = object_urls
        return context


class CfgMixin(object):
    model = UF
    success_url = reverse_lazy('UF-listar')
    paginate_by = 10


class Listar(CfgMixin, ContextMixin, ListView):
    pass


class Adicionar(CfgMixin, ContextMixin, MessageMixin, CreateView):
    success_message = u'UF adicionado com êxito'
    template_name = 'crud/object_form.html'


class Detalhes(CfgMixin, ContextMixin, DetailView):
    pass


class Editar(CfgMixin, ContextMixin, MessageMixin, UpdateView):
    success_message = u'UF atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(CfgMixin, ContextMixin, MessageMixin, DeleteView):
    success_message = u'UF excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'
