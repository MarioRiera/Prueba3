from django.urls import path
from .views import login, register

urlpatterns = [
    path('login/',login, name="login"),
    path('login/register.html/',register, name="register"),
]