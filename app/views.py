from django.shortcuts import render
from .models import *

# As views são responsáveis por receber as requisições do usuário e retornar uma resposta
# As views podem retornar um template renderizado, um JSON, um XML, um arquivo, ou qualquer outra resposta HTTP
# As views executam as regras de negócio da aplicação (ação do usuário) e interagem com o banco de dados

# Create your views here.

# Função home
def home(request):
    user = request.user # Obtendo o usuário logado
    context = {'user': user} # Criando um dicionário com o usuário logado para passar para o template

    return render(request, 'home.html', context) # Retornando o template index.html renderizado com o contexto (usuário logado)

# Função livros
def livros(request):
    livros = Livro.objects.all() # Obtendo todos os livros do banco de dados
    context = {'livros': livros} # Criando um dicionário com os livros para passar para o template

    return render(request, 'livros.html', context) # Retornando o template livros.html renderizado com o contexto (livros)

# Função cadastro
def cadastro(request):
    if request.method == 'GET': # Verificando se a requisição é do tipo GET
        autores = Autor.objects.all() # Obtendo todos os autores do banco de dados
        context = {'autores': autores} # Criando um dicionário com os autores para passar para o template (Permite preencher o campo de seleção de autores no formulário)

        return render(request, 'cadastro_de_livros.html', context) # Retornando o template cadastro_de_livros.html renderizado com o contexto (autores)

    elif request.method == 'POST': # Verificando se a requisição é do tipo POST
        titulo = request.POST.get('titulo') # Obtendo o título do livro do formulário através do atributo 'name' do input
        autor_id = request.POST.get('autor')  # Obtendo o ID do autor selecionado no formulário através do atributo 'name' do input
        data_publicacao = request.POST.get('data_publicacao') # Obtendo a data de publicação do livro do formulário através do atributo 'name' do input

        # Criando um novo livro com os dados recebidos
        livro = Livro.objects.create(
            titulo=titulo, # Atribuindo o título do livro
            autor_id=autor_id, # Atribuindo o ID do autor
            data_publicacao=data_publicacao # Atribuindo a data de publicação do livro
        )

        livro.save()

        return render(request, 'cadastro_de_livros.html') # Retornando o template cadastro_de_livros.html renderizado