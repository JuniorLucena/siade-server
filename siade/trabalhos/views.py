from datetime import date
from django.db.models import Count
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .forms import IniciarCicloForm, TrabalhoForm
from .models import Ciclo, Trabalho


def gerenciar_ciclo(request):
    trabalhos = Trabalho.objects.filter(ciclo=Ciclo.atual())\
        .annotate(total_imoveis=Count('quadras__lados__imoveis'))
    context = RequestContext(request, {
        'trabalhos': trabalhos
    })
    return render_to_response('trabalhos/gerenciar_ciclo.html', context)


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


def encerrar_ciclo(request):
    ciclo = Ciclo.atual()
    ciclo.fechado_em = date.today()
    ciclo.save()
    return redirect(reverse('ciclo:gerenciar'))


def distribuir_trabalhos(request):
    if request.method == 'POST':
        form = TrabalhoForm(request.POST)
        if form.is_valid():
            instance = form.save(False)
            instance.ciclo = Ciclo.atual()
            instance.save()
            form.save_m2m()
            return redirect(reverse('ciclo:distribuir_trabalhos'))
    else:
        form = TrabalhoForm()

    trabalhos = Trabalho.objects.filter(ciclo=Ciclo.atual())\
        .annotate(total_imoveis=Count('quadras__lados__imoveis'))
    context = RequestContext(request, {
        'form': form,
        'trabalhos': trabalhos
    })
    return render_to_response('trabalhos/distribuir_trabalhos.html', context)
