from django.urls import path
from .views import home,inicio, galeria, nosotros

urlpatterns = [
    path('',home, name="home"),
    path('index.html/',inicio, name="index"),
    path('galeria.html/',galeria, name="galeria"),
    path('nosotros.html/',nosotros, name="nosotros"),
]