from django.contrib import admin
from .models import Departamento, Noticia, Pessoa, Tag, MensagemDeContato

@admin.register(Departamento,Noticia,Pessoa, Tag, MensagemDeContato)
class NoticiaAdmin(admin.ModelAdmin):
    pass
class MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)