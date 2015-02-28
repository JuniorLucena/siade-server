from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from ..utils import render_html_or_pdf
from ..forms import D1Form


@login_required
def d1_form(request):
    if request.method == 'POST':
        form = D1Form(request.POST)
        if form.is_valid():
            return redirect(reverse('relatorios:relatorio_D1'))
    else:
        form =  D1Form()
    return render(request, 'relatorios/d1_form.html', {'form':form})
