from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    nome = models.CharField('Nome',max_length=124)
    data_de_nascimento = models.DateField('Data de nascimento', blank=True, null='True')
    telefone_celular = models.CharField('Telefone celular', max_length=15, help_text='Numero de telefone celular no formato (99) 99999-9999', null=True, blank=True)
    telefone_fixo = models.CharField('Telefone celular', max_length=15, help_text='Numero de telefone fixo no formato (99) 9999-9999', null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)
    cpf = models.CharField('CPF', max_length=14, help_text='CPF no formato 999.999.999-99')

    def __str__(self):
        return self.nome

class Obra(models.Model):
    nome = models.CharField('Nome', max_length=124)
    ano = models.CharField('Ano da obra', max_length=4)
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    tipo = models.CharField('Tipo de obra', max_length=20)

    def __str__(self):
        return self.nome

class Area_Exposicao(models.Model):
    obras = models.ManyToManyField(Obra)
    nome = models.CharField('Nome da area', max_length=124)
    descricao = models.TextField(max_length=1024)


class Exposicao(models.Model):
    areas_expo = models.ManyToManyField(Area_Exposicao)

    class Meta:
        verbose_name = 'Exposicao'
        verbose_name_plural = 'Exposicoes'

    nome = models.CharField('Nome da exposicao', max_length=124)
    descricao = models.CharField('Descricao da exposicao', max_length=2500)
    data_inic_exposicao = models.DateField('Data de inicio')
    data_fim_expo = models.DateField('Data de fim da exposicao')

    def __str__(self):
        return self.nome
