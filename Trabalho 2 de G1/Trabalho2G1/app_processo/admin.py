from django.contrib import admin
from .models import Pessoa, Departamento, Processo, EnvioProcesso, Documentos, Instauracao, PedidoPrazo, Tramitacao, Funcionario

@admin.register(Pessoa, Departamento, Processo, EnvioProcesso, Documentos, Instauracao, PedidoPrazo, Tramitacao, Funcionario)
class processoAdmin(admin.ModelAdmin):
    pass