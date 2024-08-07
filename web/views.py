from django.shortcuts import render ,redirect
from .models import tartas, ContactForm

from .forms import ContactFormForm , ContactFormModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    mistartas=tartas.objects.filter(is_private=False)
    return render(request,'index.html',{'tartaletas':mistartas})

def acerca (request):
    return render (request,"acerca.html")

@login_required
def bienvenido (request):
    tartas_privados = tartas.objects.filter(is_private=True)
    return render (request,"bienvenido.html",{'tartaletas':tartas_privados})


def contacto(request):
    if request.method == "POST":
        # form = ContactFormForm(request.POST)
        form=ContactFormModelForm(request.POST)
        if form.is_valid():
           # form.save()
           contact_form = ContactForm.objects.create(**form.cleaned_data)             

        # contact_form.save()
        return HttpResponseRedirect('/exito')  #(reverse('exito'))  # Redirige a la misma página después de enviar el formulario
    else:
        # form = ContactFormForm()
        form = ContactFormModelForm()
    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def tartas_view(request):
    tartas = tartas.objects.all()
    return render(request, 'tartas.html', {'tartas': tartas})

def quienes_somos_view(request):
    return render(request, 'quienes_somos.html')
