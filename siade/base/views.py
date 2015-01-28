from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm

from django.shortcuts import render_to_response, get_object_or_404
import shortuuid


def qrcode(request):
    qtd = int(request.GET.get('qtd', 10))
    qrcodes = [shortuuid.uuid() for i in range(qtd)]
    return render_to_response("qrcode.html", {'qrcodes': qrcodes})


@login_required
def home(request):
    return TemplateResponse(request, "home.html", {})


@sensitive_post_parameters()
@csrf_protect
@login_required
def password_reset(request, user=None):
    user_model = get_user_model()
    user_obj = get_object_or_404(user_model, pk=user)
    if request.method == "POST":
        form = AdminPasswordChangeForm(user=user_obj, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(
                reverse('agentes:agente:detalhes', args=[user]))
    else:
        form = AdminPasswordChangeForm(user=request.user)
    context = {
        'form': form,
        'title': 'Redefinir senha',
    }
    return TemplateResponse(request, 'registration/password_change_form.html',
                            context)
