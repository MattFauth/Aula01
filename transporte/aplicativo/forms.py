from django import forms
from .models import Solicitacao, Veiculo, Pessoa

class SolicitacaoForm(forms.Form):
    dia_hora = forms.DateTimeField(widget=forms.DateTimeInput())
    quantidade_pessoas = forms.IntegerField()
    origem = forms.CharField(max_length=100)
    destino = forms.CharField(max_length=100)

    def clean(self):
        dados = super().clean()

        return dados


class AtendimentoForm(forms.Form):
    solicitacao = forms.ModelChoiceField(queryset=Solicitacao.objects.all())
    motorista = forms.ModelChoiceField(queryset=Pessoa.objects.all())
    veiculo = forms.ModelChoiceField(queryset=Veiculo.objects.all())

    def clean(self):
        dados = super().clean()

        return dados