from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField('Nome', null=True, blank=True, max_length=246)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome

class PessoaJuridica(Pessoa):
    cnpj = models.CharField('CNPJ', null=True, blank=True, help_text='CNPJ no formato 00.000.000/0000-00', max_length=18)
    razao = models.CharField('Razao Social', null=True, blank=True)

class PessoaFisica(Pessoa):
    cpf = models.CharField('CPF', null=True, blank=True, help_text='CPF no formato 000.000.000-00', max_length=14)

class Evento(models.Model):
    nome = models.TextField('Nome', null=True, blank=True, max_length=124)
    eventoPrincipal = models.TextField('Evento principal', null=True, blank=True,max_length=30)
    sigla = models.TextField('Sigla', null=True, blank=True)
    dataeHoraInicio = models.DateTimeField('Data de Inicio', null=True, blank=True)
    palavrasChave = models.TextField('Palavras-Chave', null=True, blank=True, max_length=256)
    logotipo = models.CharField('Link do logotipo', null=True, blank=True, max_length=256)
    realizador = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.SET_NULL)
    cidade = models.CharField('Cidade', max_length=124)
    uf = models.CharField('UF', max_length=2, null=True, blank=True)
    endereco = models.CharField('Endereco do evento', null=True, blank=True, max_length=256)
    cep = models.CharField('CEP', null=True, blank=True, help_text='CEP no formato 00000-000', max_length=9)

    def __str__(self):
        return self.nome

class EventoCietifico(Evento):
    issn = models.CharField('ISSN', null=True, blank=True, help_text='ISSN no formato 0000-0000', max_length=9)

class Autor(Pessoa):
    curriculo = models.TextField('Curriculo', null=True, blank=True)

class ArtigoCientifico(models.Model):
    titulo = models.CharField('Titulo do artigo', null=True, blank=True, max_length=150)
    autor = models.ForeignKey(Autor, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo
