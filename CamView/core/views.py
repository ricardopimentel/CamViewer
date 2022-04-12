from django.http import Http404, StreamingHttpResponse
from django.shortcuts import render, redirect, resolve_url as r, render_to_response

from CamView.core.camera import CamView
from CamView.core.models import Camera, Pessoa, Camera_Grupo, Grupo


def Home(request):
    try:# Verificar se usuario esta logado
        if request.session['nomesugestao']:
            idpessoa = Pessoa.objects.get(usuario=request.session['userl'])
            return render(request, 'index.html', {'err': '', 'itemselec': 'HOME',})

    except KeyError:
        return redirect(r('Login'))


def Visualizacao(request, id):
    try:# Verificar se usuario esta logado
        if request.session['nomesugestao']:
            if id == 'vazio':
                grupos = Grupo.objects.all()
                return render(request, 'visualizacao.html', {'err': '', 'itemselec': 'VISUALIZAR', 'titulo': 'Selecione um grupo', 'grupos': grupos})
            else:
                camerasgrupos = Camera_Grupo.objects.filter(id_grupo=id)
                return render(request, 'visualizacao.html', {'err': '', 'itemselec': 'VISUALIZAR', 'titulo': 'Visualização de Câmeras', 'cameras': camerasgrupos})

    except KeyError:
        return redirect(r('Login'))


def VisualizarUma(request, id):
    try:# Verificar se usuario esta logado
        if request.session['nomesugestao']:
            camera = Camera.objects.get(id=id)
            return render(request, 'visualizar1.html', {'err': '', 'itemselec': 'VISUALIZAR', 'titulo': 'Selecione um grupo', 'camera': camera})

    except KeyError:
        return redirect(r('Login'))


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def VisualizarCamera(request, id):
    camera = Camera.objects.get(id=id)
    return StreamingHttpResponse(gen(CamView(camera.usuario, camera.senha, camera.ip)),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
