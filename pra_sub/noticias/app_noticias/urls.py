from django.urls import path
from .views import noticias_resumo, HomePageView, noticias_get, noticia_detalhes, ContatoSucessoView, ContatoView

urlpatterns = [
    path('', HomePageView.as_view(), name='inicio'),
    path('noticias/resumo/', noticias_resumo, name='resumo'),
    path('noticias/todas/', noticias_get, name='todas'),
    path('noticias/<int:noticia_id>/', noticia_detalhes, name='detalhes'),
    path('noticias/contato', ContatoView.as_view(), name='contato'),
    path('noticias/sucessocontato/', ContatoSucessoView.as_view(), name='contato_sucesso')
]
