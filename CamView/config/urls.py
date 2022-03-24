from django.conf.urls import url

from CamView.config import views

urlpatterns = [
    url(r'^$', views.Administracao, name='Administracao'),
    url(r'^activedirectory/$', views.Dados_ad, name='ConfigAD'),
    url(r'^configuracaoinicial/$', views.ConfigInicial, name='ConfigInicial'),
    url(r'^gerenciarpessoas/$', views.GerenciarPessoas, name='GerenciarPessoas'),
    url(r'^gerenciarcameras/$', views.GerenciarCameras, name='GerenciarCameras'),
    url(r'^gerenciargrupos/$', views.GerenciarGrupos, name='GerenciarGrupos'),
    url(r'^visualizar/$', views.Visualizar, name='Visualizar'),
    url(r'^cadastropessoa/(?P<id>.+)$', views.CadastroPessoa, name='CadastroPessoa'),
    url(r'^cadastrocameras/(?P<id>.+)$', views.CadastroCameras, name='CadastroCameras'),
    url(r'^gerenciargrupos/(?P<id>.+)$', views.CadastroGrupos, name='CadastroGrupos'),
]
