# -*- coding: utf-8 -*-
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.utils.view_urls import registry
from siade.utils.fields import ReadOnlyField
from siade.mixins.messages import MessageMixin
from ..models import Quadra, Bairro, Imovel


class QuadraMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Quadra
    success_url = reverse_lazy('quadra-listar')
    permission_required = 'imoveis.can_change_quadra'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(QuadraMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model.__name__.lower()
        return context


class Adicionar(QuadraMixin, MessageMixin, CreateView):
    success_message = u'Quadra criada com êxito'

    def get_form(self, form_class):
        id_bairro = self.kwargs.get('bairro')
        self.bairro = Bairro.objects.get(pk=id_bairro)

        form_kwargs = self.get_form_kwargs()
        form = form_class(**form_kwargs)
        form.fields['bairro'] = ReadOnlyField(initial=self.bairro)

        return form

    def get_success_url(self):
        return reverse_lazy('quadra-detalhes', kwargs={'pk': self.object.id})

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
                lado = self.object.lados.all()[0]
            imoveis = Imovel.objects.filter(lado=lado)
            context['imovel_list'] = imoveis
            context['lado'] = lado

        context['lado_list'] = lados
        return context


class Editar(QuadraMixin, MessageMixin, UpdateView):
    success_message = u'Quadra atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(QuadraMixin, MessageMixin, DeleteView):
    permission_required = 'imoveis.can_delete_quadra'
    success_message = u'Quadra excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'

registry.register_actions(
    'quadra',
    ('adicionar', Adicionar.as_view(),
        r'^adicionar/(?P<bairro>\d+)/$'),
    ('detalhes', Detalhes.as_view(), (
        r'^(?P<pk>\d+)/(?P<lado>\d+)/$',
        r'^(?P<pk>\d+)/$',
    )),
    ('editar', Editar.as_view()),
    ('excluir', Excluir.as_view())
)
urls = registry.get_urls_for_model('quadra')
