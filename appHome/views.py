from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

#importa a função get_template() do módulo loader
from django.template import loader

from appHome.forms import FormUser

#importa o modelo a ser enviado para a página 'home.html'
from appHome.models import Usuario

def add_user(request):
    #recebe os dados do form ou o form em branco
    formUser = FormUser(request.POST or None)

    #se o form foi postado
    if request.POST:
        #se os dados do post são válidos
        if formUser.is_valid():
            #salva os dados
            formUser.save()
            #exibir confirmação de cadastro
            messages.success(request, 'Usuário adicionado com sucesso!')
            #retorna para a página home
            return redirect('appHome')

    #se form em branco, cria o dicionário de dados do form
    context = {
        'form' : formUser
    }

    #renderiza o template com o form em branco
    return render(request, 'add_user.html', context)

def appHome(request):
    # carrega o template home.html
    template = loader.get_template("home.html")

    # Crie o contexto com dados se necessário
    context = {}  # Se não precisar de dados específicos, um dicionário vazio pode ser suficiente.

    # Renderiza o template com o contexto
    return HttpResponse(template.render(context, request))


def listUsers(request):
    # Cria um objeto com todos os valores do modelo.
    userList = Usuario.objects.all().values()

    # Cria um dicionário que contém o objeto
    context = {
        'users': userList
    }

    # Carrega o template list_users.html
    template = loader.get_template("list_users.html")

    # Renderiza o template com o contexto
    return HttpResponse(template.render(context, request))
