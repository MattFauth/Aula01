from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    data_nascimento = models.DateField()
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    setor_transporte = models.BooleanField()
    motorista = models.BooleanField()

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    capacidade = models.IntegerField()
    placa = models.CharField(max_length=7)


class Solicitacao(models.Model):
    solicitante = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.SET_NULL)
    dia_hora = models.DateTimeField(null=True, blank=True)
    quantidade_pessoas = models.IntegerField(null=True, blank=True)
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    atendida = models.BooleanField(null=True, blank=True)


class Atendimento(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, null=True, blank=True, on_delete=models.SET_NULL)
    motorista = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.SET_NULL)
    veiculo = models.ForeignKey(Veiculo, null=True, blank=True, on_delete=models.SET_NULL)