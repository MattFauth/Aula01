from django.shortcuts import render
from django.http import HttpResponse
from .models import Processo


def initial(request):
    valor = Processo.objects.all()
    return render(request,'app_processo/primeira.html',{'valor': valor})

def processo_detalher(request, processo_id):
    try:
        processo = Processo.objects.get(pk=processo_id)
    except Processo.DoesNotExist:
        raise Http404('Processo nao encontrado')
    return render(request, 'app_noticias/detalhes.html',
     {'processo': processo})