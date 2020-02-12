from django.shortcuts import render,reverse
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, ListView, FormView
from .models import Pessoa, Ingresso, Inscricao, Evento
from .forms import PessoaForm, IngressoForm, EventoForm, InscricaoForm
from datetime import date, datetime

def eventos_futuros(request):
    hoje = datetime.now()
    todos = Evento.objects.filter(data_inicio__gt=hoje).order_by('data_inicio')
    return render(request, 'evento/eventos_futuros.html', {'todos':todos})

def evento_detalhe(request, evento_id):
    try:
        evento = Evento.objects.get(pk=evento_id)
    except Evento.DoesNotExist:
        raise Http404('Evento nao encontrado')
    return render(request, 'evento/detalhe_evento.html', {'evento':evento})

class HomePageView(TemplateView):
    template_name = 'evento/index.html'

class PessoaView(FormView):
    template_name = 'evento/cad_pessoa.html'
    form_class = PessoaForm

    def form_valid(self, form):
        dados = form.clean()
        pessoa = Pessoa(
            nome=dados['nome'],
            email=dados['email'],
            usuario=dados['usuario'],
            cpf=dados['cpf'])
        pessoa.save()
        return super().form_valid()

    def get_success_url(self):
        return reverse('pessoa_sucesso')


class PessoaSucessoView(TemplateView):
    template_name='evento/pessoa_sucesso.html'


class EventoView(FormView):
    template_name = 'evento/cad_evento.html'
    form_class = EventoForm

    def form_valid(self, form):
        dados = form.clean()
        evento = Evento(
            nome=dados['nome'],
            sigla=dados['sigla'],
            data_inicio=dados['data_inicio'],
            realizador=dados['realizador'],
            descricao=dados['descricao']
        )
        evento.save()
        return super().form_valid()

    def get_success_url(self):
        return reverse('evento_sucesso')


class EventoSucessoView(TemplateView):
    template_name='evento/evento_sucesso.html'


class IngressoView(FormView):
    template_name = 'evento/cad_ingresso.html'
    form_class = IngressoForm

    def form_valid(self, form):
        dados = form.clean()
        ingresso = Ingresso(
            descricao=dados['descricao'],
            valor=dados['valor'],
            evento=dados['evento']
        )
        ingresso.save()
        return super().form_valid()

    def get_success_url(self):
        return reverse('ingresso_sucesso')

class IngressoSucessoView(TemplateView):
    template_name='evento/ingresso_sucesso.html'