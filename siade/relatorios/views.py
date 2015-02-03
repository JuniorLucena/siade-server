# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.db.models import Sum, Count
from .utils import html2pdf_link_callback
from siade.imoveis.models import Quadra, Bairro
from django import forms


def render_response(templateName, data, context=None, fmt='pdf'):
    if fmt == 'pdf':
        from xhtml2pdf.document import pisaDocument
        html = render_to_string(templateName, data, context)
        pdf = pisaDocument(html, link_callback=html2pdf_link_callback)
        if not pdf.err:
            return HttpResponse(pdf.dest.getvalue(),
                                content_type='application/pdf')
        else:
            return HttpResponse('We had some errors<pre>%s</pre>' %
                                     cgi.escape(html))
    else:
        return render_to_response(templateName, data, context)


@login_required
def rel_quadra(request, fmt='pdf'):
    context = {
        'range': range(20),
        'lados': range(4)
    }
    return render_response('relatorios/quadra.html', context, fmt=fmt)


@login_required
def casas_pendentes(request, fmt='pdf'):
    context = {
        'range': range(100),
    }
    return render_response('relatorios/casas_pendentes.html', context, fmt=fmt)


@login_required
def rel_diario(request, ano, mes, dia, fmt='pdf'):
    return render_response('relatorios/diario.html', {}, fmt=fmt)


@login_required
def rel_semanal(request, semana, fmt='pdf'):
    return render_response('relatorios/semana.rml', {}, fmt=fmt)


def estatisticas_bairro(request):
    bairros = [(bairro.id, bairro.nome) for bairro in Bairro.objects.all()]

    class PesquisaForm(forms.Form):
        bairro = forms.fields.ChoiceField(choices=bairros)

    bairro_id = request.GET.get('bairro')
    if bairro_id:
        form = PesquisaForm(request.GET)
        quadras = Quadra.objects.filter(bairro=bairro_id)
        quadras = quadras.annotate(total_imoveis=Count('lados__imoveis')) \
                         .annotate(pe=Sum('lados__imoveis__ponto_estrategico')) \
                         .annotate(habitantes=Sum('lados__imoveis__habitantes')) \
                         .annotate(caes=Sum('lados__imoveis__caes')) \
                         .annotate(gatos=Sum('lados__imoveis__gatos'))
    else:
        form = PesquisaForm(request.GET)
        quadras = []

    return render(request, 'relatorios/bairro.html', {
        'quadras': quadras,
        'form': form,
    })


def estatisticas_agente(request):

    bairros = [(bairro.id, bairro.nome) for bairro in Bairro.objects.all()]

    class PesquisaForm(forms.Form):
        bairro = forms.fields.ChoiceField(choices=bairros)

    bairro_id = request.GET.get('bairro')
    
    form = PesquisaForm(request.GET)

    return render(request, 'relatorios/relatorio_agente.html', {
        'bairros': bairros,
        'form': form,
    })