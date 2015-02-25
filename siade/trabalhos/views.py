from datetime import date
from django.db.models import Count
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from .forms import IniciarCicloForm, TrabalhoForm
from .models import Ciclo
from siade.agentes.models import Agente


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

    context = RequestContext(request, {'form': form})
    return render_to_response('trabalhos/iniciar_ciclo.html', context)


@permission_required('trabalhos.change_ciclo', raise_exception=True)
def encerrar_ciclo(request):
    ciclo = Ciclo.atual()
    if request.method == 'POST':
        ciclo.fechado_em = date.today()
        ciclo.save()
        return redirect(reverse('ciclo:gerenciar'))
    else:
        context = RequestContext(request, {
            'ciclo': ciclo,
        })
        return render_to_response('trabalhos/encerrar_ciclo.html', context)


@permission_required('trabalhos.change_ciclo', raise_exception=True)
def distribuir_trabalhos(request):
    ciclo = Ciclo.atual()

    agente_id = request.GET.get('agente') or request.POST.get('agente')
    if request.method == 'POST':
        form = TrabalhoForm(agente_id, request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('ciclo:distribuir_trabalhos'))
    else:
        form = TrabalhoForm(agente_id)

    agentes = Agente.objects.filter(tipo=Agente.Tipo.AgenteCampo)

    imoveis = dict(Agente.objects.filter(trabalhos__ciclo=ciclo)\
        .annotate(total=Count('trabalhos__quadra__lados__imoveis'))\
        .values_list('id', 'total'))

    for a in agentes:
        a.total_imoveis = imoveis.get(a.id, 0)

    context = {
        'form': form,
        'agentes': agentes,
    }
    return render(request, 'trabalhos/distribuir_trabalhos.html', context)
