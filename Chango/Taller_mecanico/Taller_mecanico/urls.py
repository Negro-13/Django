from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def pagina_principal(request):
    return render(request, 'pagina_principal.html')

def login(request):
    return render(request, 'login.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_principal, name='home'),
    path('login/', login, name='login'),
]
