
from django.urls import path
from .views import home, inicio, galeria, nosotros, formulario, formulario_mod

urlpatterns = [
    path('',home, name="home"),
    path('index.html/',inicio, name="index"),
    path('galeria.html/',galeria, name="galeria"),
    path('nosotros.html/',nosotros, name="nosotros"),
    path('formulario.html/', formulario, name="formulario"),
    path('formulario_mod.html/<id>', formulario_mod, name="formulario_mod")
    
]