from django.conf.urls import url
from django.urls import path

from CamView.core import views

urlpatterns = [
    url(r'^$', views.Home, name='Home'),
    url(r'^login/$', views.Home, name='Login'),
    url(r'^visualizar/$', views.Visualizacao, name='Visualizar'),
	path('visualizar_camera/(?P<id>.+)', views.VisualizarCamera, name='VisualizarCamera'),
]
