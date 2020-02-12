import logging

from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect

from django.db.models import Q
from django.template.defaultfilters import slugify

from django.views.generic.base import View
from django.views.generic import (
    ListView, FormView, DetailView, 
    FormView,TemplateView, CreateView, 
    UpdateView, DeleteView
)

from .forms import AuthRegisterForm
from django.contrib.auth.models import User
from .models import Solicitacao, Funcionario, Departamento, Atendimento


def Lista(request):
    solicitacao = Solicitacao.objects.filter(func__user=request.user)
    return render(request, 'app_empresa/solicitacoes.html', {'solicitacao': solicitacao})