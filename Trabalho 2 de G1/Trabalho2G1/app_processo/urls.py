from django.urls import path, include
from .views import initial
urlpatterns = [
    path('', initial, name='primeiro'),
]