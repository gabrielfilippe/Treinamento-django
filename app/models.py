from django.db import models

# Create your models here.

# Classe Autor (Tabela Autor no banco de dados)
class Autor(models.Model):
    nome = models.CharField(max_length=255) # Atributo nome da tabela Autor com tamanho máximo de 255 caracteres
    sobrenome = models.CharField(max_length=255) # Atributo sobrenome da tabela Autor com tamanho máximo de 255 caracteres
    email = models.EmailField() # Atributo email da tabela Autor do tipo EmailField

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

# Classe Livro (Tabela Livro no banco de dados)
class Livro(models.Model):
    titulo = models.CharField(max_length=255) # Atributo titulo da tabela Livro com tamanho máximo de 255 caracteres
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) # Atributo autor da tabela Livro do tipo ForeignKey que referencia a tabela Autor
    data_publicacao = models.DateField() # Atributo data_publicacao da tabela Livro do tipo DateField

    def __str__(self):
        return self.titulo