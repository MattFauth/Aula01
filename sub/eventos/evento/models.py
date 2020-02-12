from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    class Meta:
        verbose_name='Pessoa'
        verbose_name_plural='Pessoas'

    nome = models.TextField('Nome', max_length=128, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    usuario = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
    cpf = models.TextField('CPF', help_text='No formato 999.999.999-99', max_length=14, blank=True, null=True)

    def __str__(self):
        return self.nome
 

class Evento(models.Model):
    class Meta:
        verbose_name='Evento'
        verbose_name_plural='Eventos'

    nome = models.TextField('Nome', max_length=128, blank=True, null=True)
    sigla = models.TextField('Sigla', max_length=10, blank=True, null=True)
    data_inicio = models.DateField('Data de inicio', blank=True, null=True)
    realizador = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, blank=True, null=True)
    descricao = models.TextField('Descricao do evento', max_length=1500, blank=True, null=True)

    def __str__(self):
        return self.nome
    

class Ingresso(models.Model):
    class Meta:
        verbose_name='Ingresso'
        verbose_name_plural='Ingressos'
    
    descricao = models.TextField('Descricao do ingresso', max_length=300, blank=True, null=True)
    valor = models.FloatField('Valor do ingresso', blank=True, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return 'Ingresso numero {} do evento {}'.format(self.pk, self.evento.nome)
    

class Inscricao(models.Model):
    class Meta:
        verbose_name='Inscricao'
        verbose_name_plural='Inscricoes'
    
    pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, blank=True, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, blank=True, null=True)
    ingresso = models.ForeignKey(Ingresso, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return 'Ingresso de {} para o evento {}'.format(self.pessoa.nome, self.evento.nome)
    