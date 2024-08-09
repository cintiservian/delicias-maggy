from django.shortcuts import render ,redirect, get_object_or_404
from .models import tartas, ContactForm, Favoritos 
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
        form = ContactFormForm(request.POST)
        #form=ContactFormModelForm(request.POST)
        if form.is_valid():
           # form.save()
           contact_form = ContactForm.objects.create(**form.cleaned_data)             

        # contact_form.save()
        return HttpResponseRedirect('/exito')  #(reverse('exito'))  # Redirige a la misma página después de enviar el formulario
    else:
        form = ContactFormForm()
        #form = ContactFormModelForm()
    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def tartas_view(request):
    tartas = tartas.objects.all()
    return render(request, 'tartas.html', {'tartas': tartas})

def quienes_somos_view(request):
    return render(request, 'quienes_somos.html')

def tarta_detalle(request, tarta_id):
    tarta = get_object_or_404(tartas,pk=tarta_id)
    return render(request,'tarta_detalle.html',{'tarta':tarta})

def lista_favorito(request):
    favoritos= Favoritos.objects.filter(user=request.user)
    return render(request,'favoritos.html',{'lista_favoritos':favoritos})

@login_required
def agregarFavorito(request, tarta_id):
    tarta_favorita = get_object_or_404(tartas, id=tarta_id)
    favorite, created = Favoritos.objects.get_or_create(user=request.user, tarta=tarta_favorita)
    if created:
        # El flan se ha añadido a favoritos
        pass
    url_previa = request.META.get('HTTP_REFERER', 'default_url')
    return redirect(url_previa)

