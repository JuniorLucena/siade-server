# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.utils.view_urls import registry
from siade.mixins.messages import MessageMixin
from ..models import Municipio


class MunicipioMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Municipio
    success_url = reverse_lazy('municipio-listar')
    permission_required = 'imoveis.can_change_municipio'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(MunicipioMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model.__name__.lower()
        return context


class Listar(MunicipioMixin, ListView):
    pass


class Adicionar(MunicipioMixin, MessageMixin, CreateView):
    template_name = 'crud/object_form.html'


class Detalhes(MunicipioMixin, DetailView):
    pass


class Editar(MunicipioMixin, MessageMixin, UpdateView):
    success_message = u'Municipio atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(MunicipioMixin, MessageMixin, DeleteView):
    permission_required = 'imoveis.can_delete_municipio'
    success_message = u'Municipio excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'

registry.register_actions(
    'municipio',
    ('listar', Listar.as_view()),
    ('adicionar', Adicionar.as_view()),
    ('detalhes', Detalhes.as_view()),
    ('editar', Editar.as_view()),
    ('excluir', Excluir.as_view())
)
urls = registry.get_urls_for_model('municipio')
