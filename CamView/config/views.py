import sys

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, resolve_url as r

from CamView.config.forms import AdForm, PessoaForm
from CamView.core.models import Config, Pessoa


def Administracao(request):
    if dict(request.session).get('nomesugestao'):
        return render(request, 'config/visualizacao.html', {
            'title': 'Administração',
            'itemselec': 'ADMINISTRAÇÃO',
        })
    return redirect(r('Login'))

def Dados_ad(request):
    if not dict(request.session).get('nomesugestao'):
        return redirect(r('Login'))

    if dict(request.session).get('usertip') == 'admin':
        try:
            model = (Config.objects.get(id=1))
            # Vefirica se veio aolgo pelo POST
            if request.method == 'POST':
                # cria uma instancia do formulario de preenchimento dos dados do AD com os dados vindos do request POST:
                form = AdForm(request, data=request.POST)
                # Checa se os dados são válidos:
                if form.is_valid():
                    # Chama a página novamente
                    messages.success(request, 'Configurações salvas com sucesso!')
                return render(request, 'config/admin_config_ad.html', {'form': form})
            else:
                form = AdForm(request, initial={
                    'dominio': model.dominio,
                    'endservidor': model.endservidor,
                    'gadmin': model.gadmin,
                    'ou': model.ou, 'filter': model.filter
                })
                return render(request, 'config/admin_config_ad.html', {
                    'title': 'Config. LDAP',
                    'itemselec': 'ADMINISTRAÇÃO',
                    'form': form,
                })
        except ObjectDoesNotExist:
            model = ''
            messages.error(request, sys.exc_info())
            return redirect(r('Administracao'))
    else:
        messages.error(request, "Você não tem permissão para acessar essa página, redirecionando para HOME")
        return redirect(r('Home'))

def ConfigInicial(request):
    form = AdForm(request)
    if request.method == 'POST':
        # cria uma instancia do formulario de preenchimento dos dados do AD com os dados vindos do request POST:
        form = AdForm(request, data=request.POST)
        # Checa se os dados são válidos:
        if form.is_valid():
            return redirect(r('Login'))
    return render(request, 'config/admin_config_ad_inicial.html', {
        'title': 'Config. Inicial',
        'itemselec': 'ADMINISTRAÇÃO',
        'form': form,
    })

def GerenciarPessoas(request):
    pessoas = Pessoa.objects.all().exclude(usuario='000000')
    if dict(request.session).get('nomesugestao'):
        return render(request, 'config/gerenciar_pessoa.html', {
            'title': 'Administração',
            'itemselec': 'ADMINISTRAÇÃO',
            'pessoas': pessoas,
        })
    return redirect(r('Login'))

def CadastroPessoa(request, id):
    if dict(request.session).get('nomesugestao'):
        editar =False

        if id == 'cadastro': # verifica se é para cadastrar ou alterar
            form = PessoaForm(request)
        else: # se for para alterar cria um formulário já preenchido
            editar = True
            pessoa = Pessoa.objects.get(id=id)
            form = PessoaForm(request, initial={'nome': pessoa.nome, 'usuario': pessoa.usuario, 'status': pessoa.status, 'email': pessoa.email})

        if request.method == 'POST':
            if editar:
                pessoa = Pessoa.objects.get(id=id)
                form = PessoaForm(request, request.POST, instance=pessoa)
            else:
                form = PessoaForm(request, request.POST)
            # Checa se os dados são válidos:
            if form.is_valid():
                if editar:
                    pessoa.nome = request.POST['nome']
                    pessoa.usuario = request.POST['usuario']
                    if dict(request.POST).get('status'):
                        pessoa.status = request.POST['status']
                    else:
                        pessoa.status = False
                    pessoa.email = request.POST['email']
                    pessoa.save()
                else:
                    form.save()
                messages.success(request, "Sucesso!")
                return redirect(r('GerenciarPessoas'))
        return render(request, 'config/admin_cadastro_pessoa.html', {
            'title': 'Administração',
            'itemselec': 'ADMINISTRAÇÃO',
            'id': id,
            'titulo': 'Cadastro de Pessoas',
            'form': form,
        })
    return redirect(r('Login'))

def Visualizar(request):
    if dict(request.session).get('nomesugestao'):
        return render(request, 'config/visualizacao.html', {
            'title': 'Administração',
            'itemselec': 'ADMINISTRAÇÃO',
        })
    return redirect(r('Login'))