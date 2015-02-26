from shortuuid import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from ..utils import render_html_or_pdf


@login_required
def qrcode_print(request, fmt='html'):
    qtd = int(request.GET.get('qtd', 10))
    qrcodes = [uuid() for i in range(qtd)]
    return render_html_or_pdf(request, 'qrcode/print.html',
                              {'qrcodes': qrcodes}, fmt=fmt)


@login_required
def qrcode_form(request):
    return render(request, 'qrcode/form.html', {})


@login_required
def qrcode_img(request):
    text = request.GET.get('text', 'no text')
    response = HttpResponse(content_type='image/png')
    import qrcode
    from qrcode import make as make_qrcode
    img = make_qrcode(text)
    img.save(response)
    return response
