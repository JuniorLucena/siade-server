# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.mixins.messages import MessageMixin
from ..models import Logradouro


class LogradouroMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Logradouro
    permission_required = 'imoveis.change_logradouro'
    raise_exception = True
    paginate_by = 50
    success_url = reverse_lazy('%s:logradouro:listar'
                               % model._meta.app_label)

    def get_context_data(self, **kwargs):
        context = super(LogradouroMixin, self).get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name.capitalize()
        context['object_class'] = self.model
        return context


class Listar(LogradouroMixin, ListView):
    pass


class Adicionar(LogradouroMixin, MessageMixin, CreateView):
    success_message = u'Logradouro adicionado com êxito'
    template_name = 'crud/object_form.html'


class Detalhes(LogradouroMixin, DetailView):
    pass


class Editar(LogradouroMixin, MessageMixin, UpdateView):
    success_message = u'Logradouro atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(LogradouroMixin, MessageMixin, DeleteView):
    permission_required = "imoveis.can_delete_logradouro"
    success_message = u'Logradouro excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'


urls = patterns(
    '',
    url(r'^$', Listar.as_view(), name='listar'),
    url(r'^adicionar/$', Adicionar.as_view(), name='adicionar'),
    url(r'^(?P<pk>\w+)/$', Detalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>\w+)/editar$', Editar.as_view(), name='editar'),
    url(r'^(?P<pk>\w+)/excluir$', Excluir.as_view(), name='excluir')
)
