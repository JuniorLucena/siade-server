# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from django.db.models import Count
from django.views.generic import (UpdateView)
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.forms.models import modelform_factory
from siade.trabalhos.forms import CicloDatePicker
from .forms import IniciarCicloForm, TrabalhoForm
from .models import Ciclo, Trabalho, Visita
from siade.agentes.models import Agente
from braces.views import LoginRequiredMixin, PermissionRequiredMixin


@permission_required('trabalhos.change_ciclo', raise_exception=True)
def gerenciar_ciclo(request):
    ciclo = Ciclo.atual()

    if not ciclo:
        return render(request, 'trabalhos/nenhum_ciclo.html')

    agentes = Agente.objects.filter(tipo=Agente.Tipo.AgenteCampo)

    imoveis = dict(Agente.objects.filter(trabalhos__ciclo=ciclo)\
        .annotate(total=Count('trabalhos__quadra__lados__imoveis'))\
        .values_list('id', 'total'))

    vistas = dict(Agente.objects.filter(visitas__ciclo=ciclo)\
        .annotate(total=Count('visitas__imovel')).values_list('id', 'total'))

    for a in agentes:
        a.total_imoveis = imoveis.get(a.id, 0)
        a.total_visitas = vistas.get(a.id, 0)
        if a.total_imoveis > 0:
            percentual = float(a.total_visitas / float(a.total_imoveis))
            a.percentual = int(round(percentual * 100))
        else:
            a.percentual = 0

    context = {
        'ciclo' : ciclo,
        'agentes': agentes
    }
    return render(request, 'trabalhos/gerenciar_ciclo.html', context)


@permission_required('trabalhos.change_ciclo', raise_exception=True)
def iniciar_ciclo(request):
    if request.method == 'POST':
        form = IniciarCicloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('ciclo:distribuir_trabalhos'))
    else:
        form = IniciarCicloForm()

    context = {'form': form}
    return render(request, 'trabalhos/ciclo_form.html', context)


@permission_required('trabalhos.change_ciclo', raise_exception=True)
def encerrar_ciclo(request):
    ciclo = Ciclo.atual()
    if request.method == 'POST':
        ciclo.fechado_em = date.today()
        ciclo.save()
        return redirect(reverse('ciclo:gerenciar'))
    else:
        context = {
            'ciclo': ciclo,
        }
        return render(request, 'trabalhos/encerrar_ciclo.html', context)


@permission_required('trabalhos.change_ciclo', raise_exception=True)
def distribuir_trabalhos(request):
    ciclo = Ciclo.atual()

    agente_id = request.GET.get('agente') or request.POST.get('agente')
    if agente_id:
        context = trabalhos_alterar(request)
    else:
        context = {}

    agentes = Agente.objects.filter(tipo=Agente.Tipo.AgenteCampo)

    imoveis = dict(Agente.objects.filter(trabalhos__ciclo=ciclo)\
        .annotate(total=Count('trabalhos__quadra__lados__imoveis'))\
        .values_list('id', 'total'))

    for a in agentes:
        a.total_imoveis = imoveis.get(a.id, 0)

    context.update({'agentes': agentes})
    return render(request, 'trabalhos/distribuir_trabalhos.html', context)


@permission_required('trabalhos.change_ciclo', raise_exception=True)
def trabalhos_remover(request, pk):
    return_to = request.META.get('HTTP_REFERER', 'ciclo:distribuir_trabalhos')
    get_object_or_404(Trabalho, pk=pk).delete()
    return redirect(return_to)


def trabalhos_alterar(request, *args, **kwargs):
    agente_id = request.GET.get('agente') or request.POST.get('agente')
    agente = get_object_or_404(Agente, pk=agente_id)
    if request.method == 'POST':
        form = TrabalhoForm(agente, request.POST)
        if form.is_valid():
            # Guardar quantas quadras foram digitadas no form
            n_quadras = len(form.cleaned_data.get('quadras'))
            # salvar o form
            form.save()
            # Verificar quantas quadras foram relamente incluidas
            n_incluidas = len(form.cleaned_data.get('quadras'))
            # Se for diferente emitir um aviso
            if n_quadras != n_incluidas:
                messages.warning(request, 'Algumas quadras não foram incluídas.')

            form = TrabalhoForm(agente)
    else:
        form = TrabalhoForm(agente)
    context = {'form': form}
    return context


class AlterarCiclo(LoginRequiredMixin, PermissionRequiredMixin, UpdateView ):
    model = Ciclo
    success_message = u'Ciclo atualizado com êxito'
    form_class = modelform_factory(Ciclo, fields=("data_fim",), widgets={"data_fim": CicloDatePicker()})
    success_url = reverse_lazy('ciclo:gerenciar')
    permission_required = 'trabalhos.change_ciclo'
    raise_exception = True


def listar_imoveis_visitados(request, pk):

    agente = get_object_or_404(Agente, pk=pk)

    visitas = Visita.objects.all()\
        .filter(agente=agente)\
        .filter(ciclo=Ciclo.atual())

    context = {
        'agente': agente,
        'visitas': visitas
    }

    return render(request, 'trabalhos/listar_imoveis_visitados.html', context)
