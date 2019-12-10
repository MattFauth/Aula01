from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=)
    nome = models.TextField('Nome do autor', max_length=120, null=True, blank=True)
    matricula = models.TextField('Matricula do autor', max_length=120, null=Ture, blank=True)

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    titulo = models.TextField('Titulo da noticia', max_length=120, null=True, blank=True)
    conteudo = models.TextField('Conteudo da noticia', null=True, blank=True)
    data = models.DateTimeField()