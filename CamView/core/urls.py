from django.conf.urls import url
from django.urls import path

from CamView.core import views

urlpatterns = [
    url(r'^$', views.Home, name='Home'),
    url(r'^login/$', views.Home, name='Login'),
    #url(r'^visualizar/$', views.Visualizacao, name='Visualizar'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    path('mask_feed', views.mask_feed, name='mask_feed'),
	#path('visualizar_camera/(?P<id>.+)', views.VisualizarCamera, name='VisualizarCamera'),
]
