from decimal import Decimal
from django.shortcuts import redirect, render
from .models import *

# As views são responsáveis por receber as requisições do usuário e retornar uma resposta
# As views podem retornar um template renderizado, um JSON, um XML, um arquivo, ou qualquer outra resposta HTTP
# As views executam as regras de negócio da aplicação (ação do usuário) e interagem com o banco de dados

# Create your views here.

# Função home
def home(request):
    user = request.user # Obtendo o usuário logado
    livros = Livro.objects.all() # Obtendo todos os livros do banco de dados
    # Criando um dicionário com o usuário logado para passar para o template
    context = {
        'user': user,
        'livros': livros
    } 

    return render(request, 'home.html', context) # Retornando o template index.html renderizado com o contexto (usuário logado)

# Função livros
def livros(request):
    livros = Livro.objects.all() # Obtendo todos os livros do banco de dados
    context = {'livros': livros} # Criando um dicionário com os livros para passar para o template

    return render(request, 'livros.html', context) # Retornando o template livros.html renderizado com o contexto (livros)

# Função cadastro
def cadastro(request):
    autores = Autor.objects.all() # Obtendo todos os autores do banco de dados
    # Criando um dicionário com os autores para passar para o template (Permite preencher o campo de seleção de autores no formulário)
    context = {
        'autores': autores
    } 
    if request.method == 'GET': # Verificando se a requisição é do tipo GET
        return render(request, 'cadastro_de_livros.html', context) # Retornando o template cadastro_de_livros.html renderizado com o contexto (autores)

    elif request.method == 'POST': # Verificando se a requisição é do tipo POST
        titulo = request.POST.get('titulo') # Obtendo o título do livro do formulário através do atributo 'name' do input
        autor_id = request.POST.get('autor')  # Obtendo o ID do autor selecionado no formulário através do atributo 'name' do input
        data_publicacao = request.POST.get('data_publicacao') # Obtendo a data de publicação do livro do formulário através do atributo 'name' do input
        valor = str(request.POST.get('valor')) # Obtendo o valor do livro do formulário através do atributo 'name' do input
        status = request.POST.get('status') # Obtendo o status do livro do formulário através do atributo 'name' do input
        imagem = request.FILES.get('imagem') # Obtendo a imagem do livro do formulário através do atributo 'name' do input
    
        # Criando um novo livro com os dados recebidos
        livro = Livro.objects.create(
            titulo=titulo, # Atribuindo o título do livro
            autor_id=autor_id, # Atribuindo o ID do autor
            data_publicacao=data_publicacao, # Atribuindo a data de publicação do livro
            livro_valor= Decimal(valor.replace(',', '.')), # Atribuindo o valor do livro
            status=status, # Atribuindo o status do livro
            imagem=imagem # Atribuindo a imagem do livro


        )
        livro.save()

        return redirect('livros') # Redirecionando para a rota livros
    
# Função editar
def editar(request, id):
    livro = Livro.objects.get(id=id) # Obtendo o livro com o ID recebido
    autores = Autor.objects.all() # Obtendo todos os autores do banco de dados
    data_publicacao_formatada = livro.data_publicacao.strftime('%Y-%m-%d') # Formatando a data de publicação do livro
    valor_formatado = str(livro.livro_valor)

    # Criando um dicionário com o livro e autores para passar para o template
    context = {
        'livro': livro,
        'autores': autores,
        'data_publicacao_formatada': data_publicacao_formatada,
        'valor_formatado': valor_formatado,
    }

    if request.method == 'GET': # Verificando se a requisição é do tipo GET
        return render(request, 'editar_livro.html', context) # Retornando o template editar_livro.html renderizado com o contexto (livro e autores)
    
    elif request.method == 'POST': # Verificando se a requisição é do tipo POST
        titulo = request.POST.get('titulo') # Obtendo o título do livro do formulário através do atributo 'name' do input
        autor_id = request.POST.get('autor') # Obtendo o ID do autor selecionado no formulário através do atributo 'name' do input
        data_publicacao = request.POST.get('data_publicacao') # Obtendo a data de publicação do livro do formulário através do atributo 'name' do input
        valor = request.POST.get('valor')
        status = request.POST.get('status') # Obtendo o status do livro do formulário através do atributo 'name' do input
        imagem = request.FILES.get('nova_imagem') # Obtendo a imagem do livro do formulário através do atributo 'name' do input


        livro.titulo = titulo # Atribuindo o novo título ao livro
        livro.autor_id = autor_id # Atribuindo o novo ID do autor ao livro
        livro.data_publicacao = data_publicacao # Atribuindo a nova data de publicação ao livro
        livro.livro_valor = Decimal(valor.replace(',', '.')) # Atribuindo o novo valor ao livro
        livro.status = status
        if imagem:
            livro.imagem = imagem
        livro.save() # Salvando as alterações no banco de dados

        return redirect('livros') # Redirecionando para a rota livros
    
# Função excluir
def excluir(request, id):
    livro = Livro.objects.get(id=id) # Obtendo o livro com o ID recebido
    livro.delete() # Deletando o livro do banco de dados

    return redirect('livros') # Redirecionando para a rota livros

