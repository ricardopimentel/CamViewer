from django.http import Http404, StreamingHttpResponse
from django.shortcuts import render, redirect, resolve_url as r, render_to_response

# Create your views here.
from django.template import RequestContext

from CamView.core.camera import VideoCamera, IPWebCam, MaskDetect, LiveWebCam
from CamView.core.models import Camera, Pessoa

def Home(request):
    try:# Verificar se usuario esta logado
        if request.session['nomesugestao']:
            idpessoa = Pessoa.objects.get(usuario=request.session['userl'])
            return render(request, 'index.html', {'err': '', 'itemselec': 'HOME',})

    except KeyError:
        return redirect(r('Login'))


def index(request):
    return render(request, 'streamapp/home.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def webcam_feed(request):
    return StreamingHttpResponse(gen(IPWebCam()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def mask_feed(request):
    return StreamingHttpResponse(gen(MaskDetect()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def livecam_feed(request):
    return StreamingHttpResponse(gen(LiveWebCam()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
