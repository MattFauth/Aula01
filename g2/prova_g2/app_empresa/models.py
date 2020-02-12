from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Cargo(models.Model):
    nome = models.TextField('Nome do cargo', max_length=120, null=True, blank=True)
    ehchefe = models.BooleanField('Eh chefe?', null=True, blank=True)
    ehmotorista = models.BooleanField('Eh motorista?', null=True, blank=True)
    ehtransp = models.BooleanField('Eh Chefe do transporte?', null=True, blank=True)

class Departamento(models.Model):
    nome = models.TextField('Nome do departamento', max_length=120, null=True, blank=True)
    codigo = models.TextField('Codigo do departamento', max_length=4, null=True, blank=True)
    ehTransp = models.BooleanField('Eh transporte?', null=True, blank=True)

class Veiculo(models.Model):
    placa = models.TextField('Placa do carro', max_length=8, help_text='No formato AAA-0000', null=True, blank=True)
    descricao = models.TextField('Descricao do veiculo', max_length=500, null=True, blank=True)

class Funcionario(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, blank=True)
    dep = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.TextField('Nome do funcionario', max_length=120, null=True, blank=True)
    matricula = models.TextField('Matricula do funcionario', max_length=6, null=True, blank=True)

class Solicitacao(models.Model):
    func = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    origem = models.TextField('Origem da viagem', max_length=120, null=True, blank=True)
    destino = models.TextField('Destino da viagem', max_length=120, null=True, blank=True)
    data = models.DateTimeField('Data e hora da viagem', null=True, blank=True)
    qtppl = models.TextField('Quantidade de passageiros', max_length=1)

class Atendimento(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True, blank=True)
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.SET_NULL, null=True, blank=True)
    funcio = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)