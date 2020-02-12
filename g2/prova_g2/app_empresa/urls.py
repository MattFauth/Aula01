from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from .views import (Lista)

app_name='app_empresa'

urlpatterns = [
    path('solicitacoes', Lista, name='solicitacoes'),
    ]
