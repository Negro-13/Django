from django.shortcuts import render

def hola_mundo(request):
    return render(request, 'Taller_mecanico/hola_mundo.html')

def pagina_principal(request):
    return render(request, 'Taller_mecanico/pagina_principal.html')

def login(request):
    return render(request, 'Taller_mecanico/login.html')

def administracion(request):
    return render(request, 'Taller_mecanico/administracion.html')

def presupuesto(request):
    return render(request, 'Taller_mecanico/presupuesto.html')

def quienes_somos(request):
    return render(request, 'Taller_mecanico/quienes_somos.html')

def servicios(request):
    return render(request, 'Taller_mecanico/servicios.html')

def ubicacion_contacto(request):
    return render(request, 'Taller_mecanico/ubicacion_contacto.html')
