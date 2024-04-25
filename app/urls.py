from django.urls import path
from app.views import *


urlpatterns = [
    path('', home, name='home'),
    path('livros/', livros, name='livros'),
    path('cadastro_de_livros/', cadastro_de_livros, name='cadastro_de_livros'),
]