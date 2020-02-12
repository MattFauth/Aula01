from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    nome = models.CharField('Nome', max_length=128)
    data_de_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    telefone_celular = models.CharField('Telefone celular', max_length=15, help_text='Numero do telefone celular no formato (99) 99999-9999', null=True, blank=True,)
    telefone_fixo = models.CharField('telefone fixo', max_length=14, help_text='Numero do telefone fixo no formato (99) 9999-9999', null=True, blank=True,)
    email = models.EmailField('E-mail', null=True, blank=True)
    cpf = models.CharField('CPF', max_length=14, help_text='CPF no formato 999.999.999-99', blank=True, null=True)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    nome_noticia = models.CharField(max_length=50)
    conteudo = models.TextField()
    data_noticia = models.DateTimeField()

    def __str__(self):
        return self.nome_noticia