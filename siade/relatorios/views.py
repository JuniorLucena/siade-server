from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
import trml2pdf


def render_to_pdf_response(templateName, data, context=None):
    rml = render_to_string(templateName, data, context)
    pdfData = trml2pdf.parseString(rml)
    response = HttpResponse(mimetype='application/pdf')
    response.write(pdfData)
    return response


@login_required
def rel_diario(request, ano, mes, dia):
    return render_to_pdf_response('relatorios/teste.rml', {})


@login_required
def rel_semanal(request, semana):
    return render_to_pdf_response('relatorios/teste.rml', {})
