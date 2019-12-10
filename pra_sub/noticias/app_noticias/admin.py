from django.contrib import admin
from .models import Departamento, Autor, Noticia, Pessoa, Tag

@admin.register(Departamento,Autor,Noticia,Pessoa, Tag)
class NoticiaAdmin(admin.ModelAdmin):
    pass