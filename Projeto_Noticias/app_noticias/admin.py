from django.contrib import admin
from .models import Noticia, Pessoa, Tag



@admin.register(Noticia,Pessoa,Tag)
class NoticiaAdmin(admin.ModelAdmin):
    pass
