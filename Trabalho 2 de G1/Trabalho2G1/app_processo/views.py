from django.shortcuts import render
from django.http import HttpResponse
from .models import Processo
from .forms import ContatoForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


def initial(request):
    valor = Processo.objects.all()
    return render(request,'app_processo/primeira.html',{'valor': valor})

def processo_detalhe(request, processo_id):
    try:
        processo = Processo.objects.get(pk=processo_id)
    except Processo.DoesNotExist:
        raise Http404('Processo nao encontrado')
    return render(request, 'app_processo/detalhes.html',
     {'processo': processo})


class ContatoView(FormView):
    template_name = 'app_processo/contato.html'
    form_class = ContatoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = MensagemDeContato(nome=dados['nome'],
         email=dados['email'], mensagem=dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contato_sucesso')

    
class ContatoSucessoView(TemplateView):
    template_name = 'app_processo/contato_sucesso.html'