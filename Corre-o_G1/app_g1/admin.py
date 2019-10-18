from django.contrib import admin
from .models import Pessoa, Funcionario, Departamento, Processo, Documento, Portaria, PedidoPrazo, Envio, Tramitacao

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Departamento)
admin.site.register(Documento)
admin.site.register(Portaria)
admin.site.register(Processo)
admin.site.register(PedidoPrazo)
admin.site.register(Envio)
admin.site.register(Tramitacao)

class PessoaAdmin(admin.ModelAdmin):
    pass
class FuncionarioAdmin(admin.ModelAdmin):
    pass
class DepartamentoAdmin(admin.ModelAdmin):
    pass
class DocumentoAdmin(admin.ModelAdmin):
    pass
class PortariaAdmin(admin.ModelAdmin):
    pass
class ProcessoAdmin(admin.ModelAdmin):
    pass
class PedidoPrazoAdmin(admin.ModelAdmin):
    pass
class EnvioAdmin(admin.ModelAdmin):
    pass

class TramitacaoAdmin(admin.ModelAdmin):
    pass