from django.contrib import admin
from .models import Cargo, Departamento, Veiculo, Funcionario, Solicitacao, Atendimento

@admin.register(Cargo, Departamento, Veiculo, Funcionario, Solicitacao, Atendimento)
class processoAdmin(admin.ModelAdmin):
    pass