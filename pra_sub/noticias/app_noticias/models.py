from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    nome = models.TextField('Nome do autor', max_length=120, null=True, blank=True)
    data_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    tel_cel = models.CharField('Telefone Celular', max_length=15, help_text='Numero no formato (99) 99999-9999', blank=True, null=True)
    email = models.EmailField('Endereco de email', blank=True, null=True)

    def __str__(self):
        return self.nome    

class Tag(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)    

    def __str__(self):
        return self.nome
    

class Departamento(models.Model):
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    nome = models.TextField('Nome do departamento', max_length=120)

    def __str__(self):
        return self.nome
class Autor(models.Model):
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    pessoa = models.OneToOneField(Pessoa, on_delete=models.SET_NULL, blank=True, null=True)
    matricula = models.TextField('Matricula do autor', max_length=120, null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Departamento')

    def __str__(self):
        return self.pessoa.__str__()

class Noticia(models.Model):
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    titulo = models.TextField('Titulo da noticia', max_length=120, null=True, blank=True)
    conteudo = models.TextField('Conteudo da noticia', null=True, blank=True)
    data = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.titulo

class MensagemDeContato(models.Model):
    class Meta:
            verbose_name = 'Mensagem de contato'
            verbose_name_plural = 'Mensagens de contato'

    nome = models.CharField('Nome', max_length=128, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True, blank=True, null=True)
