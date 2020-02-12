from django import forms
from .models import Pessoa, Ingresso, Evento, User

class PessoaForm(forms.Form):
    nome = forms.CharField(max_length=128, min_length=4)
    email = forms.EmailField(required=False)
    usuario = forms.ModelChoiceField(queryset=User.objects.all())
    cpf = forms.CharField(max_length=14, min_length=14)

    def clean(self):
        dados=super().clean()
        email=dados.get('email', None)
        nome=dados.get('nome', None)
        usuario=dados.get('usuario', None)

        nomes_ruins = ['Piroka','ppk', 'Reprovar']
        for nomin in nomes_ruins:
            if nome in nomin.lower():
                self.add_error('nome', 'Nome tem palavra nao permitida')
        return dados

class EventoForm(forms.Form):
    nome = forms.CharField(max_length=128, min_length=4)
    sigla = forms.CharField(max_length=128, min_length=2)
    data_inicio = forms.DateField(widget=forms.DateTimeInput())
    realizador = forms.ModelChoiceField(queryset=Pessoa.objects.all())
    descricao = forms.CharField(widget=forms.Textarea)

    def clean(self):
        dados=super().clean()
        nome=dados.get('nome', None)
        sigla=dados.get('sigla', None)
        data_inicio=dados.get('data_inicio', None)
        realizador=dados.get('realizador', None)
        descricao=dados.get('descricao', None)
        palavras = ['porra', 'mortes', 'assassinato']
        for palavra in palavras:
            if palavra in descricao.lower():
                self.add_error('descricao', 'Descricao tem palavra nao permitida')
        return dados


class IngressoForm(forms.Form):
    descricao = forms.CharField(widget=forms.Textarea)
    valor = forms.FloatField()
    evento = forms.ModelChoiceField(queryset=Evento.objects.all())

    def clean(self):
        dados=super().clean()
        descricao=dados.get('descricao',None)
        valor=dados.get('valor',None)
        evento=dados.get('evento',None)
        palavras = ['porra', 'mortes', 'assassinato']
        for palavra in palavras:
            if palavra in descricao.lower():
                self.add_error('descricao', 'Descricao tem palavra nao permitida')
        return dados

class InscricaoForm(forms.Form):
    evento = forms.ModelChoiceField(queryset=Evento.objects.all())
    ingresso = forms.ModelChoiceField(queryset=Ingresso.objects.all())

    def clean(self):
        dados=super().clean()
        evento=dados.get('evento',None)
        ingresso=dados.get('ingresso',None)
        return dados