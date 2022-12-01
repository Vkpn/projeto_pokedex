
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pagina_inicial.urls')),
    path('admin/', admin.site.urls),
]
