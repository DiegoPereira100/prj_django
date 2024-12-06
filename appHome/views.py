from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from PIL import Image, ImageDraw, ImageFont
from django.db.models import Count
from django.contrib.auth import authenticate, login

import io
import base64

#importa a função get_template() do módulo loader
from django.template import loader

#importa os forms a serem utilizados
from appHome.forms import FormUser, FormCourse, FormLogin

#importa o modelo a ser enviado para a página 'home.html'
from appHome.models import Usuario, Curso, Login, Venda

from datetime import timedelta, datetime

from django.db import transaction

def buy_course(request, course_id):
    # Verifica se o curso existe
    try:
        curso = Curso.objects.get(id=course_id)
    except Curso.DoesNotExist:
        messages.error(request, 'Curso não encontrado.')
        return redirect('list_courses')

    # Verifica se há estoque disponível
    if curso.stock <= 0:
        messages.error(request, 'Este curso está fora de estoque.')
        return redirect('list_courses')

    usuario = None  #
    # Atualiza o estoque do curso
    curso.stock -= 1
    curso.save()

    # Cria a venda com o campo 'quantidade'
    with transaction.atomic():
        venda = Venda.objects.create(usuario=usuario, curso=curso, quantidade=1)

    messages.success(request, f'Compra realizada com sucesso! Você comprou o curso "{curso.name}".')
    return redirect('list_courses')

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

def delete_user(request, id_user):

    user = Usuario.objects.get(id=id_user)

    user.delete()

    return redirect('appHome')


def edit_user(request, id_user):

    user = Usuario.objects.get(id=id_user)

    form = FormUser(request.POST or None, instance=user)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('appHome')
    context = {
        'form' : form
    }
    return render(request, 'edit_user.html', context)



def add_course(request):
    # Se o método for POST, processa o formulário
    if request.method == 'POST':
        formCourse = FormCourse(request.POST)  # Cria a instância com os dados POST

        # Verifica se o formulário é válido
        if formCourse.is_valid():
            formCourse.save()  # Salva o curso no banco de dados
            messages.success(request, 'Curso cadastrado com sucesso!')
            return redirect('appHome')  # Redireciona para a página de cursos ou outra página após sucesso

        # Se o formulário não for válido, adiciona mensagens de erro
        else:
            messages.error(request, 'Erro ao cadastrar curso. Verifique os campos.')

    # Se o método for GET, simplesmente cria um formulário vazio
    else:
        formCourse = FormCourse()

    # Contexto para o template
    context = {
        'form': formCourse
    }

    # Renderiza o template com o formulário
    return render(request, 'add_course.html', context)


def appHome(request):
    #Recupera o email do usuário da sessão, se estiver presente
    user_email = request.session.get('email')

    context = {
        'user_email': user_email
    }

    return render(request, "home.html", context)


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


def listCourses(request):
    # Cria um objeto com todos os valores do modelo.
    courseList = Curso.objects.all().values()

    # Cria um dicionário que contém o objeto
    context = {
        'courses': courseList
    }

    # Carrega o template list_courses.html
    template = loader.get_template("list_courses.html")

    # Renderiza o template com o contexto
    return HttpResponse(template.render(context, request))


def makeLogin(request):
    formL = FormLogin(request.POST or None)

    if request.method == 'POST' and formL.is_valid():
        # Obtenha os dados do formulário
        _email = formL.cleaned_data.get('email')
        _password = formL.cleaned_data.get('password')

        # Tenta autenticar o usuário com base no email e senha
        userL = authenticate(request, username=_email, password=_password)

        if userL is not None:
            login(request, userL)  # Faz login no sistema
            return redirect('appHome')  # Redireciona para a página inicial
        else:
            return render(request, 'login.html', {'formLogin': formL, 'error_message': 'Credenciais inválidas. Por favor, tente novamente.'})

    # Se o método não for POST ou o formulário não for válido
    context = {
        'formLogin': formL
    }

    return render(request, 'login.html', context)


def sales_report(request):
    # Recupera todas as vendas feitas no mês atual
    current_month = datetime.now().month
    current_year = datetime.now().year
    vendas = Venda.objects.filter(data_venda__month=current_month, data_venda__year=current_year)

    
    # Relatório geral de vendas
    total_sales = vendas.count()
    total_revenue = sum([venda.curso.price for venda in vendas])

    # Vendas por curso
    vendas_por_curso = vendas.values('curso__name').annotate(count=Count('curso')).order_by('-count')

    # Gerar gráfico de vendas por curso com Pillow
    courses = [v['curso__name'] for v in vendas_por_curso]
    sales_count = [v['count'] for v in vendas_por_curso]

    # Tamanho da imagem
    img_width = 600
    img_height = 400

    # Criar uma imagem branca
    image = Image.new('RGB', (img_width, img_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Definir fonte para o gráfico
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    except IOError:
        font = ImageFont.load_default()

    # Configurar cores
    bar_color = (50, 150, 255)
    text_color = (0, 0, 0)

    # Configurar as barras do gráfico
    max_height = img_height - 100  # espaço para título e legenda
    bar_width = 40
    bar_gap = 50

    # Calcular a altura de cada barra proporcionalmente ao número de vendas
    max_sales = max(sales_count) if sales_count else 1
    for i, (course, count) in enumerate(zip(courses, sales_count)):
        bar_height = int((count / max_sales) * max_height)
        x1 = i * (bar_width + bar_gap) + 50  # Espaço inicial
        y1 = img_height - bar_height - 50  # posição y para as barras
        x2 = x1 + bar_width
        y2 = img_height - 50
        
        # Desenhar barra
        draw.rectangle([x1, y1, x2, y2], fill=bar_color)
        
        # Desenhar o texto da barra (nome do curso)
        draw.text((x1 + 5, y2 + 5), course, fill=text_color, font=font)

        # Desenhar a quantidade de vendas em cima da barra
        draw.text((x1 + 5, y1 - 20), str(count), fill=text_color, font=font)

    # Adicionar título
    draw.text((img_width // 2 - 80, 10), f'Vendas por Curso - {datetime.now().strftime("%B %Y")}', fill=text_color, font=font)

    # Salvar imagem em base64 para o template
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)
    graph_url = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    context = {
        'total_sales': total_sales,
        'total_revenue': total_revenue,
        'graph_url': graph_url,
    }

    return render(request, 'sales_report.html', context)