from django.contrib import admin
from .models import Pessoa, Ingresso, Evento, Inscricao

@admin.register(Pessoa, Ingresso, Evento, Inscricao)
class NoticiaAdmin(admin.ModelAdmin):
    pass