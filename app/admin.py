from django.contrib import admin
from app.models import *

# Register your models here.

class AutorAdmin(admin.ModelAdmin): #deixando em forma de tabela no admin, deixando bonitin
    list_display = ('nome', 'sobrenome', 'email')
    search_fields = ('nome', 'sobrenome')

class LivroAdmin(admin.ModelAdmin): #deixando em forma de tabela no admin, deixando bonitin
    list_display = ('titulo', 'autor', 'data_publicacao')
    search_fields = ('titulo', 'autor')

admin.site.register(Autor, AutorAdmin) #registrando o modelo Autor na area de administração
admin.site.register(Livro, LivroAdmin)
