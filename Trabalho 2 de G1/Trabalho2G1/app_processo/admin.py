from django.contrib import admin
from .models import Pessoa, Departamento, Processo, EnvioProcesso, Documentos, Instauracao, PedidoPrazo, Tramitacao

@admin.register(Pessoa, Departamento, Processo, EnvioProcesso, Documentos, Instauracao, PedidoPrazo, Tramitacao)
class processoAdmin(admin.ModelAdmin):
    pass