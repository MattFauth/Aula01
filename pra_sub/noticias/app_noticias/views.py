from django.http import HttpResponse, Http404
from django.shortcuts import render, reverse
from .models import Noticia, MensagemDeContato
from .forms import ContatoForm
from django.views.generic import TemplateView, ListView, FormView

def noticias_resumo(request):
    total = Noticia.objects.count()
    return render(request, 'app_noticias/resumo.html', {'total':total})

def noticias_get(request):
    todas = Noticia.objects.all()
    return render(request, 'app_noticias/todas.html', {'todas':todas})

def noticia_detalhes(request, noticia_id):
    try:
        noticia = Noticia.objects.get(pk=noticia_id)
    except Noticia.DoesNotExist:
        raise Http404('Noticia nao encontrada')
    return render(request, 'app_noticias/detalhes.html', {'noticia':noticia})

class ContatoView(FormView):
    template_name = 'app_noticias/contato.html'
    form_class = ContatoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = MensagemDeContato(nome=dados['nome'], email=dados['email'], mensagem=dados['mensagem'])  
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contato_sucesso')

class HomePageView(TemplateView):
    template_name = 'app_noticias/inicio.html'

class ContatoSucessoView(TemplateView):
    template_name='app_noticias/contato_sucesso.html'
    