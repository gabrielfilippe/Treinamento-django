from django.urls import path
from .views import *

# Define as rotas do projeto
# Cada rota chama uma função do arquivo views.py

urlpatterns = [
    path('', home, name='home'), # Rota para a página inicial (Chama a função home do arquivo views.py)
    path('livros/', livros, name='livros'), # Rota para a página de livros (Chama a função livros do arquivo views.py)
    path('cadastro/', cadastro, name='cadastro'), # Rota para a página de cadastro (Chama a função cadastro do arquivo views.py)
    path('editar/<int:id>/', editar, name='editar'), # Rota para a página de edição (Chama a função editar do arquivo views.py)
    path('excluir/<int:id>/', excluir, name='excluir'), # Rota para a página de deleção (Chama a função deletar do arquivo views.py)
]