from django.contrib import admin
from .models import Departamento, Autor, Noticia, Pessoa, Tag, MensagemDeContato

@admin.register(Departamento,Autor,Noticia,Pessoa, Tag, MensagemDeContato)
class NoticiaAdmin(admin.ModelAdmin):
    pass
class MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)