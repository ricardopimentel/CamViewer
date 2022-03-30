from django.http import Http404, StreamingHttpResponse
from django.shortcuts import render, redirect, resolve_url as r, render_to_response

from CamView.core.camera import CamView
from CamView.core.models import Camera, Pessoa

def Home(request):
    try:# Verificar se usuario esta logado
        if request.session['nomesugestao']:
            idpessoa = Pessoa.objects.get(usuario=request.session['userl'])
            return render(request, 'index.html', {'err': '', 'itemselec': 'HOME',})

    except KeyError:
        return redirect(r('Login'))


def Visualizacao(request):
    try:# Verificar se usuario esta logado
        if request.session['nomesugestao']:
            idpessoa = Pessoa.objects.get(usuario=request.session['userl'])
            return render(request, 'visualizacao.html', {'err': '', 'itemselec': 'HOME',})

    except KeyError:
        return redirect(r('Login'))


def index(request):
    return render(request, 'streamapp/home.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def VisualizarCamera(request, id):
    camera = Camera.objects.get(id=id)
    return StreamingHttpResponse(gen(CamView(camera.usuario, camera.senha, camera.ip)),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
