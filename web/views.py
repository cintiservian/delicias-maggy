from django.shortcuts import render
from .models import tartas

# Create your views here.
def inicio(request):
    mistartas=tartas.objects.filter(is_private=False)
    return render(request,'index.html',{'tartaletas':mistartas})

def acerca (request):
    return render (request,"acerca.html")

def bienvenido (request):
    tartas_privados = tartas.objects.filter(is_private=True)
    return render (request,"bienvenido.html",{'tartaletas':tartas_privados})
