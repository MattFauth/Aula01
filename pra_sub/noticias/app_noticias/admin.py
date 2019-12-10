from django.contrib import admin
from .models import Departamento, Autor, Noticia, Pessoa

@admin.register(Departamento,Autor,Noticia,Pessoa)
class NoticiaAdmin(admin.ModelAdmin):
    pass