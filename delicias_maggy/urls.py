"""delicias_maggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web import views
from django.http import HttpResponseRedirect
from django.urls import reverse


# def exito(request):
#     return render(request, 'exito.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name="inicio"),
    path('acerca',views.acerca,name="acerca"),
    path('bienvenido',views.bienvenido,name="bienvenido"),
    path('contacto', views.contacto, name='contacto'),
    path('exito/', views.exito, name='exito'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('tartas/', views.tartas_view, name='tartas'),
    path('quienes-somos/', views.quienes_somos_view, name='quienes_somos'),
    path('tarta/<int:tarta_id>/', views.tarta_detalle, name='tarta_detalle'),
    path('favoritos/',views.lista_favorito,name='listafavoritos'),
    path('agregarFavorito/<int:tarta_id>/', views.agregarFavorito, name='agregar_favorito'),
]
