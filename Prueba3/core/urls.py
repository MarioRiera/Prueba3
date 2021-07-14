from Prueba3.api.views import formulario
from django.urls import path
from .views import home, inicio, galeria, nosotros, formulario

urlpatterns = [
    path('',home, name="home"),
    path('index.html/',inicio, name="index"),
    path('galeria.html/',galeria, name="galeria"),
    path('nosotros.html/',nosotros, name="nosotros"),
    path('formularioBD.html/',formulario, name="formulario")
    
]