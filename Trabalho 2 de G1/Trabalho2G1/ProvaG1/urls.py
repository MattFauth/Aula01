from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_processo.urls')),
    path('conta/', include('django.contrib.auth.urls')),
]
