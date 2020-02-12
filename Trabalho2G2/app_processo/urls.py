from django.urls import path, include
from .views import initial, processo_detalhe
urlpatterns = [
    path('', initial, name='primeiro'),
    path('app_processo/detalhes.html', processo_detalhe, name='detalhes')
]