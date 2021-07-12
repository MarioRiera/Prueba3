from django.urls import path
from .views import inicio, galeria, nosotros

urlpatterns = [
    path('',inicio, name="index"),
    path('galeria/',galeria, name="galeria"),
    path('nosotros/',nosotros, name="nosotros"),
]