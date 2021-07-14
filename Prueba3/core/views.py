from core.forms import VehiculoForm
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

def formulario(request):
    datos={
        'form':VehiculoForm
    }

    if request.method == 'POST':
        formu = VehiculoForm(request.POST)
        if formu.is_valid:
            formu.save()
            datos['mensaje'] = "Guardado correctamente"



    return render(request,'formulario.html',datos)

def formulario_mod(request,id):
    vehiculo = Vehiculo.objects.get(patente = id)
    datos={
        'form':VehiculoForm(instance=vehiculo)
    }
    
    return render(request,'formulario_mod.html',datos)

