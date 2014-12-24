# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum, Count
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.utils.view_urls import registry
from siade.mixins.messages import MessageMixin
from ..models import Bairro, Imovel


class BairroMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Bairro
    success_url = reverse_lazy('bairro-listar')
    permission_required = 'imoveis.can_change_bairro'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BairroMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model.__name__.lower()
        return context


class Listar(BairroMixin, ListView):
    pass


class Adicionar(BairroMixin, MessageMixin, CreateView):
    success_message = u'Bairro criado com êxito'
    template_name = 'crud/object_form.html'
    permission_required = 'imoveis.can_add_bairro'


class Detalhes(BairroMixin, DetailView):

    def get_context_data(self, **kwargs):
        quadras = self.object.quadras.all()
        quadras = quadras.annotate(total_imoveis=Count('lados__imoveis'))
        quadras = quadras.annotate(total_caes=Sum('lados__imoveis__caes'))
        quadras = quadras.annotate(total_gatos=Sum('lados__imoveis__gatos'))

        context = super(Detalhes, self).get_context_data(**kwargs)
        context.update({
            'quadra_list': quadras,
        })
        return context


class Editar(BairroMixin, MessageMixin, UpdateView):
    success_message = u'Bairro atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(BairroMixin, MessageMixin, DeleteView):
    success_message = u'Bairro excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'
    permission_required = 'imoveis.can_delete_bairro'


registry.register_actions(
    'bairro',
    ('listar', Listar.as_view()),
    ('adicionar', Adicionar.as_view()),
    ('detalhes', Detalhes.as_view()),
    ('editar', Editar.as_view()),
    ('excluir', Excluir.as_view())
)
urls = registry.get_urls_for_model('bairro')
