from django.shortcuts import render
from app.models import *

#aqui que faz as coisas, executam as funções 

def home(request):
    return render(request, 'index.html')

def livros(request):
    livros = Livro.objects.all()
    context = {
        'livros': livros
    }
    return render(request, 'livros.html', context)

def cadastro_de_livros(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        context = {
            'autores': autores
        }
    
        return render(request, 'cadastro_de_livros.html', context)
    
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor_id = request.POST.get('autor_id')  # Supondo que 'autor_id' seja o ID do autor selecionado no formulário
        data_publicacao = request.POST.get('data_publicacao')
        #Cria um novo livro com os dados recebidos
        livro = Livro.objects.create(
            titulo=titulo,
            autor_id=autor_id,
            data_publicacao=data_publicacao
        )
        livro.save()
        print(livro)
        return render(request, 'cadastro_de_livros.html')



# Create your views here.
