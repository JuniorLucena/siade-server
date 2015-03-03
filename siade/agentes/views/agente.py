# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from django.views.generic import (CreateView, ListView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.shortcuts import get_object_or_404
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from siade.mixins.messages import MessageMixin
from ..models import Agente
from ..forms import AgenteForm


class AgenteMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Agente
    form_class = AgenteForm
    permission_required = 'agentes.change_agente'
    raise_exception = True

    def get_success_url(self):
        nextUrl = self.request.GET.get('next')
        if nextUrl is None:
            app_label = self.model._meta.app_label
            nextUrl = reverse('%s:agente:definir_senha' % app_label,
                              kwargs={'pk': self.object.id})
        return nextUrl

    def get_context_data(self, **kwargs):
        context = super(AgenteMixin, self).get_context_data(**kwargs)
        context['title'] = 'Usuários'
        context['object_class'] = self.model
        context['fields'] = getattr(self, 'fields',
                                    self.model._meta.get_all_field_names())
        return context


class Listar(AgenteMixin, ListView):
    pass


class Adicionar(AgenteMixin, MessageMixin, CreateView):
    success_message = u'Agente adicionado com êxito'
    template_name = 'crud/object_form.html'


class Detalhes(AgenteMixin, DetailView):
    pass


class Editar(AgenteMixin, MessageMixin, UpdateView):
    success_message = u'Agente atualizado com êxito'
    template_name = 'crud/object_form.html'


class Excluir(AgenteMixin, MessageMixin, DeleteView):
    success_message = u'Agente excluído com êxito'
    template_name = 'crud/object_confirm_delete.html'


@sensitive_post_parameters()
@csrf_protect
@login_required
def definir_senha(request, pk=None):
    user_model = get_user_model()
    user_obj = get_object_or_404(user_model, pk=pk)
    if request.method == "POST":
        form = AdminPasswordChangeForm(user=user_obj, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(
                reverse('agentes:agente:detalhes', args=[pk]))
    else:
        form = AdminPasswordChangeForm(user=request.user)
    context = {'agente': user_obj, 'form': form, 'title': 'Redefinir senha'}
    return render(request, 'registration/password_change_form.html', context)


urls = patterns(
    '',
    url(r'^$', Listar.as_view(), name='listar'),
    url(r'^adicionar/$', Adicionar.as_view(), name='adicionar'),
    url(r'^(?P<pk>[^/]+)/$', Detalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>[^/]+)/editar$', Editar.as_view(), name='editar'),
    url(r'^(?P<pk>[^/]+)/excluir$', Excluir.as_view(), name='excluir'),
    url(r'^(?P<pk>[^/]+)/definir-senha$', definir_senha, name='definir_senha'),
)
