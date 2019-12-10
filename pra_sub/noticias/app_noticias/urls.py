from django.urls import path
from .views import noticias_resumo, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='inicio'),
    path('noticias/resumo/', noticias_resumo, name='resumo')
]
