from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def pagina_principal(request):
    return render(request, 'pagina_principal.html')

def login(request):
    return render(request, 'login.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def servicios(request):
    return render(request, 'servicios.html')

def ubicacion_contacto(request):
    return render(request, 'ubicacion_contacto.html')

def presupuesto(request):
    return render(request, 'presupuesto.html')

def administracion(request):
    return render(request, 'administracion.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_principal, name='pagina_principal'),
    path('login/', login, name='login'),
    path('quienes-somos/', quienes_somos, name='quienes_somos'),
    path('servicios/', servicios, name='servicios'),
    path('ubicacion-contacto/', ubicacion_contacto, name='ubicacion_contacto'),
    path('presupuesto/', presupuesto, name='presupuesto'),
    path('administracion/', administracion, name='administracion'),
]
