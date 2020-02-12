from django.db import models
from django.contrib.auth.models import User


class Departamento(models.Model):
    nome = models.CharField('Departamento', max_length=124, null=True, blank=True)


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=124, blank=True, null=True)
    data_de_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    telefone_celular = models.CharField('Telefone celular', max_length=15,
                                        help_text='Numero de telefone celular no formato (99) 99999-9999', null=True,
                                        blank=True)
    telefone_fixo = models.CharField('Telefone celular', max_length=15,
                                     help_text='Numero de telefone fixo no formato (99) 9999-9999', null=True,
                                     blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)
    cpf = models.CharField('CPF', max_length=14, help_text='CPF no formato 999.999.999-99', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Funcionario(Pessoa):
    matricula = models.CharField('Matricula', max_length=20, blank=True, null=True)
    funcao = models.CharField('Funcao', max_length=124, blank=True, null=True)


class Processo(models.Model):
    numero = models.CharField('Numero do processo', max_length=25, help_text='Numero no modelo 9999999.99.9999.9.99.9999', blank=True, null=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
    interessados = models.ManyToManyField(Pessoa, 'Interessados')
    investigados = models.ManyToManyField(Pessoa, 'Investigados')
    data = models.DateField('Data criacao', null=True, blank=True)

    def __str__(self):
        return self.numero


class Documentos(models.Model):
    numeroProtocolo = models.CharField('Numero de protocolo do Documento', max_length=24, null=True, blank=True)
    data = models.DateField('Data do documento', null=True, blank=True)
    processo = models.ForeignKey(Processo, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField('Nome', max_length=246, null=True, blank=True)
    descricao = models.TextField('Descricao', null=True, blank=True)

    def __str__(self):
        return self.nome + ' ' + self.numeroProtocolo


class Instauracao(Documentos):
    dataInstauracao = models.DateField('Data de instauracao', null=True, blank=True)


class PedidoPrazo(Documentos):
    prazoAnt = models.DateField('Data de prazo anterior', null=True, blank=True)
    prazoAtual = models.DateField('Date de prazo novo', null=True, blank=True)
    justificativa = models.TextField('Justificativa de Pedido', max_length=1024)


class EnvioProcesso(Documentos):
    dataEnvio = models.DateField('Data de Envio', null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)


class Tramitacao(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.SET_NULL, null=True, blank=True)
    origem = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True,related_name= 'Origem')
    destino = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True,related_name= 'Destino')
    dataMov = models.DateField('Data de movimentacao', null=True, blank=True)
