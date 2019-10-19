from django.contrib import admin
from .models import Pessoa, Departamento, Processo, EnvioProcesso, Documentos, Instauracao, PedidoPrazo, Tramitacao, Funcionario, MensagemDeContato

@admin.register(Pessoa, Departamento, Processo, EnvioProcesso, Documentos, Instauracao, PedidoPrazo, Tramitacao, Funcionario)
class processoAdmin(admin.ModelAdmin):
    pass

@admin.register(MensagemDeContato)
class MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)