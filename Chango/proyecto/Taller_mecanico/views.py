from django.shortcuts import render

def hola_mundo(request):
    return render(request, 'Taller_mecanico/hola_mundo.html')
