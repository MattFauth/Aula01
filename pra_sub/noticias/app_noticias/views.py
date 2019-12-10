from django.http import HttpResponse
from django.shortcuts import render
from .models import Noticia
from django.views.generic import TemplateView, ListView, FormView

def noticias_resumo(request):
    total = Noticia.objects.all()
    return HttpResponse(request, 'app_noticias/resumo.html', {'total':total})

class HomePageView(TemplateView):
    template_name = 'app_noticias/inicio.html'
    