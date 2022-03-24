from django.http import Http404
from django.shortcuts import render, redirect, resolve_url as r, render_to_response

# Create your views here.
from django.template import RequestContext

from CamView.core.models import Camera, Pessoa

def Home(request):
    try:# Verificar se usuario esta logado
        if request.session['nomesugestao']:
            idpessoa = Pessoa.objects.get(usuario=request.session['userl'])
            return render(request, 'index.html', {'err': '', 'itemselec': 'HOME',})

    except KeyError:
        return redirect(r('Login'))
