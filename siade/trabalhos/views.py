# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from django.db.models import Count
from django.views.generic import (UpdateView)
from django.http.response import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.forms.models import modelform_factory
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from siade.trabalhos.forms import CicloDatePicker
from .forms import IniciarCicloForm, TrabalhoForm
from .models import Ciclo, Trabalho, Visita
from siade.agentes.models import Agente
from siade.imoveis.models import Bairro, Quadra


@permission_required('trabalhos.change_ciclo', raise_exception=True)
def gerenciar_ciclo(request):
    ciclo = Ciclo.atual()

    if not ciclo:
        return render(request, 'trabalhos/nenhum_ciclo.html')

    agentes = Agente.objects.filter(tipo=Agente.Tipo.AgenteCampo)

    imoveis = dict(Agente.objects.filter(trabalhos__ciclo=ciclo)
        .annotate(total=Count('trabalhos__quadra__lados__imoveis'))
        .values_list('id', 'total'))

    vistas = dict(Agente.objects.filter(visitas__ciclo=ciclo)
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
        'ciclo': ciclo,
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
def trabalhos_alterar(request, pk=None):
    agente = get_object_or_404(Agente, pk=pk)
    if request.method == 'POST':
        form = TrabalhoForm(agente, request.POST)
        if form.is_valid():
            success_url = request.POST.get('next', reverse('ciclo:distribuir_trabalhos'))
            form.save()
            messages.success(request, 'Quadras atualizadas com sucesso.')
            return redirect(success_url)
    else:
        form = TrabalhoForm(agente)

    context = {
        'form': form,
        'agente': agente,
        'trabalhos': Trabalho.objects.filter(ciclo=Ciclo.atual(),
                                             agente=agente),
        'bairros': Bairro.objects.filter(municipio=agente.municipio),
    }
    return render(request, 'trabalhos/quadras_agente.html', context)


@permission_required('trabalhos.change_ciclo', raise_exception=True)
def trabalhos_quadras(request):
    bairro = request.GET.get('bairro')
    agente = request.GET.get('agente')
    trabalhos = Trabalho.objects.filter(ciclo=Ciclo.atual())
    exclude = trabalhos.exclude(agente=agente).values_list('quadra', flat=True)
    quadras = Quadra.objects.filter(bairro=bairro).exclude(id__in=exclude)\
            .annotate(total_imoveis=Count('lados__imoveis'))

    return JsonResponse(list(quadras.values('id', 'numero', 'bairro','total_imoveis')),
                        safe=False)


class AlterarCiclo(LoginRequiredMixin, PermissionRequiredMixin, UpdateView ):
    model = Ciclo
    success_message = u'Ciclo atualizado com êxito'
    form_class = modelform_factory(Ciclo, fields=("data_fim",), widgets={"data_fim": CicloDatePicker()})
    success_url = reverse_lazy('ciclo:gerenciar')
    permission_required = 'trabalhos.change_ciclo'
    raise_exception = True


def listar_imoveis_visitados(request, pk):
    agente = get_object_or_404(Agente, pk=pk)

    visita_list = Visita.objects.all()\
        .filter(agente=agente)\
        .filter(ciclo=Ciclo.atual())

    paginator = Paginator(visita_list, 13)

    is_paged = False
    page = request.GET.get('page')

    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    
    is_paged = paginator.num_pages > 1
    
    context = {
        'page_obj': page,
        'is_paginated' : is_paged,
        'paginator' : paginator,
        'agente': agente,
        'visitas': page.object_list
    }

    return render(request, 'trabalhos/visita_list.html', context)
