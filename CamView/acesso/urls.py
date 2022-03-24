from django.conf.urls import url
from CamView.acesso import views

urlpatterns = [
    url(r'^entrar/$', views.Login, name='Login'),
    url(r'^sair/$', views.Logout, name='Logout'),
]
