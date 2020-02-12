from django.shortcuts import render, reverse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import SolicitacaoForm, AtendimentoForm
from .models import Pessoa, Solicitacao, Atendimento


class SolicitacaoView(FormView):
    template_name = 'aplicativo/solicitacao.html'
    form_class = SolicitacaoForm

    def form_valid(self, form):
        dados = form.clean()
        solicitante = Pessoa.objects.get(usuario=self.request.user)
        solicitacao = Solicitacao(
                        solicitante=solicitante,
                        dia_hora=dados['dia_hora'],
                        quantidade_pessoas=dados['quantidade_pessoas'],
                        origem=dados['origem'],
                        destino=dados['destino']
                    )
        solicitacao.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('solicitacao_sucesso')


class SolicitacaoSucessoView(TemplateView):
    template_name = 'aplicativo/solicitacao_sucesso.html'


class AtendimentoView(FormView):
    template_name = 'aplicativo/atendimento.html'
    form_class = AtendimentoForm

    def form_valid(self, form):
        dados = form.clean()
        solicitante = Pessoa.objects.get(usuario=self.request.user)
        atendimento = Atendimento(
                        solicitacao=dados['solicitacao'],
                        motorista=dados['motorista'],
                        veiculo=dados['veiculo']
                    )
        atendimento.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('atendimento_sucesso')


class AtendimentoSucessoView(TemplateView):
    template_name = 'aplicativo/atendimento_sucesso.html'