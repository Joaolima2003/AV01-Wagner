from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.contrib.auth.models import User


def login(request): #Passa 3 campos para utilizar as messages, (request, Qual tipo de mensagem(ex: constants.SUCCESS), 'mensagem')
    if request.user.is_authenticated:
        return redirect('/plataforma/home')
    
    return render(request, 'login.html')

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/home')
    
    return render(request, 'cadastro.html')


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Email e Nome não podem está vazios.')
        return redirect('/auth/cadastro/')
    
    if len(senha) < 8:
        messages.add_message(request, constants.ERROR, 'Senha não pode ter menos de 8 caracteres.')
        return redirect('/auth/cadastro/')
    
    

    if User.objects.filter(email = email).exists():
        messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse email.')
        return redirect('/auth/cadastro/')
    
    if User.objects.filter(username = nome).exists():
        messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome.')
        return redirect('/auth/cadastro/')
    

    try:
    
        usuario = User.objects.create_user(username = nome, email = email, password = senha)

        usuario.save()

        messages.add_message(request, constants.SUCCESS, 'Cadastrado com Sucesso.')
        return redirect('/auth/cadastro/')
    
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do Sistema..')
        return redirect('/auth/cadastro/')
    

def valida_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')


    usuario =  auth.authenticate(request, username = nome, password = senha)
    

    if not usuario:
        messages.add_message(request, constants.WARNING, 'Nome ou Senha inválidos.')
        return redirect('/auth/login/')
    
    else:
        auth.login(request, usuario)
        return redirect('/plataforma/home/')
    

def sair(request):#.clear() apaga todos os dados daquela session, .flush() apaga completamente o session do usuario
    auth.logout(request)#Desloga o usuario por inteiro retirando seu sessionid que é criado quando logado // request.session.flush() request.session.get_expiry_age() indica o tempo que a session irá expirar
    return redirect('/auth/login/') #request.session.get_expiry_date() mostra a data que irá expirar