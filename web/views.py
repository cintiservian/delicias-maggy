from django.shortcuts import render ,redirect
from .models import tartas
from .forms import ContactFormForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def inicio(request):
    mistartas=tartas.objects.filter(is_private=False)
    return render(request,'index.html',{'tartaletas':mistartas})

def acerca (request):
    return render (request,"acerca.html")

def bienvenido (request):
    tartas_privados = tartas.objects.filter(is_private=True)
    return render (request,"bienvenido.html",{'tartaletas':tartas_privados})


def contacto(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
           # form.save()
           contact_form = ContactForm(
                customer_email=form.cleaned_data['customer_email'],
                customer_name=form.cleaned_data['customer_name'],
                message=form.cleaned_data['message']
            )
        contact_form.save()
        return HttpResponseRedirect('/exito')  #(reverse('exito'))  # Redirige a la misma página después de enviar el formulario
    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')
