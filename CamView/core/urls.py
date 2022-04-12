from django.conf.urls import url
from django.urls import path

from CamView.core import views

urlpatterns = [
    url(r'^$', views.Home, name='Home'),
    url(r'^login/$', views.Home, name='Login'),
    url(r'^visualizar/(?P<id>.+)$', views.Visualizacao, name='Visualizar'),
    url(r'^visualizar1/(?P<id>.+)', views.VisualizarUma, name='VisualizarUma'),
	path('visualizar_camera/(?P<id>.+)', views.VisualizarCamera, name='VisualizarCamera'),
]
