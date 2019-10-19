from django.urls import path, include
from .views import initial, processo_detalhe, ContatoView, ContatoSucessoView

urlpatterns = [
    path('', initial, name='primeiro'),
    path('processos/<int:processo_id>/', processo_detalhe, name='detalhes'),
    path('contato', ContatoView, name='contato'),
]