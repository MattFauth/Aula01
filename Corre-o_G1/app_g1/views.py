from django.shortcuts import render
from django.http import HttpResponse

from .models import Processo


def resumo_processo(request):
    total = Processo.objects.count()
