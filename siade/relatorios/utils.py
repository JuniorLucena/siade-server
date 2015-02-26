from django.shortcuts import render, HttpResponse
from django_xhtml2pdf.utils import generate_pdf
from django.template import RequestContext


def render_html_or_pdf(request, templateName, context, **kwargs):
    fmt = kwargs.get('fmt', 'pdf')
    if fmt == 'pdf':
        context = RequestContext(request, context)
        file_object = HttpResponse(content_type='application/pdf')
        return generate_pdf(templateName, file_object, context)
    else:
        return render(request, templateName, context)
