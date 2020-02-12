from django.contrib import admin
from .models import Exposicao, Pessoa, Obra, Area_Exposicao


@admin.register(Exposicao, Pessoa, Obra, Area_Exposicao)
class ExposicaoAdmin(admin.ModelAdmin):
    pass;
