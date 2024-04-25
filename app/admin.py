from django.contrib import admin
from .models import *

# Register your models here.

# Classe AutorAdmin (Tabela Autor no admin)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'email'] # Mostrando os campos nome, sobrenome e email na visualização da tabela
    search_fields = ['nome', 'sobrenome'] # Adicionando a opção de busca pelos campos nome e sobrenome

# Classe LivroAdmin (Tabela Livro no admin)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'data_publicacao'] # Mostrando os campos titulo, autor e data_publicacao na visualização da tabela
    search_fields = ['titulo', 'autor'] # Adicionando a opção de busca pelos campos titulo e autor

admin.site.register(Autor, AutorAdmin) # Registrando o modelo Autor no admin
admin.site.register(Livro, LivroAdmin) # Registrando o modelo Livro no admin