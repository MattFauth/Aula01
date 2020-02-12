from django.urls import path
from .views import HomePageView, evento_detalhe, eventos_futuros, PessoaView, EventoView, IngressoView, PessoaSucessoView, EventoSucessoView, IngressoSucessoView

urlpatterns = [
    path('', HomePageView.as_view(), name='inicio'),
    path('evento/cad_pessoa/', PessoaView.as_view(), name='cadPessoa'),
    path('evento/cad_evento/', EventoView.as_view(), name='cadEvento'),
    path('evento/cad_ingresso', IngressoView.as_view(), name='cadIngresso'),
    path('evento/sucessopesso/', PessoaSucessoView.as_view(), name='sucesspPessoa'),
    path('evento/sucessoevento/', EventoSucessoView.as_view(), name='sucessoEvento'),
    path('evento/sucessoingresso', IngressoSucessoView.as_view(), name='sucessoIngresso'),
    path('evento/<int:evento_id>/', evento_detalhe, name='detalhe'),
    path('evento/todas', eventos_futuros, name='futuro'),
]