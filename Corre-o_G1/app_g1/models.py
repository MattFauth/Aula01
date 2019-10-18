from django.contrib.auth.models import User
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    matricula = models.CharField(max_length=15)
    data_admissao = models.DateField()

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nome = models.CharField(max_length=120, null=True, blank=True)
    numero = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.nome
class Processo(models.Model):
    numero = models.CharField(max_length=120, null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, related_name='funcionario', null=True, blank=True, on_delete=models.SET_NULL)
    intere = models.ManyToManyField(Pessoa, related_name='interesados')
    inves = models.ManyToManyField(Pessoa, related_name='investigados')
    criacao = models.DateField()
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.numero

class Documento(models.Model):
    numero = models.CharField(max_length=120, null=True, blank=True)
    titulo = models.CharField(max_length=120, null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    data = models.DateField()
    processo = models.ForeignKey(Processo, null=True, blank=True, on_delete=models.SET_NULL)
    usuario = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.numero

class Portaria(Documento):
    numero_portaria = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.numero


class PedidoPrazo(Documento):
    prazo_anterior = models.DateField()
    novo_prazo = models.DateField()
    justificativa = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.numero

class Envio(Documento):
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL)
    data_envio = models.DateField()

    def __str__(self):
        return self.numero

class Tramitacao (models.Model):
    processo = models.ForeignKey(Processo, null=True, blank=True, on_delete=models.SET_NULL)
    origem = models.ForeignKey(Departamento, related_name='origem', null=True, blank=True, on_delete=models.SET_NULL)
    destino = models.ForeignKey(Departamento, related_name='destino', null=True, blank=True, on_delete=models.SET_NULL)
    data_movimentacao = models.DateField()

    def __str__(self):
        return self.processo.numero



