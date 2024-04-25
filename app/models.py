from django.db import models


# Create your models here.


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo