from core.models import Vehiculo
from django.shortcuts import render

# Create your views here.

def home(request):
    vehiculos = Vehiculo.objects.all()
    datos ={
        "vehiculos":vehiculos
    }
    return render(request,'index.html')
def inicio(request):
    return render(request,'index.html')
def galeria(request):
    return render(request,'galeria.html')
def nosotros(request):
    return render(request,'nosotros.html')



