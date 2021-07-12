from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'index.html')
def galeria(request):
    return render(request,'galeria.html')
def nosotros(request):
    return render(request,'nosotros.html')


