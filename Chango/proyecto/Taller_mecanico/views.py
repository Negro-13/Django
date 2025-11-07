from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def hola_mundo(request):
    return render(request, 'Taller_mecanico/hola_mundo.html')

def pagina_principal(request):
    return render(request, 'Taller_mecanico/pagina_principal.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bienvenido {username}!')
                return redirect('pagina_principal')
        else:
            messages.error(request, 'Usuario o contraseña inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'Taller_mecanico/login.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registro exitoso!')
            return redirect('pagina_principal')
        else:
            messages.error(request, 'Error en el registro. Por favor, verifica los datos.')
    else:
        form = UserCreationForm()
    return render(request, 'Taller_mecanico/register.html', {'form': form})
def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('pagina_principal')

@login_required
def administracion(request):
    return render(request, 'Taller_mecanico/administracion.html')

@login_required
def presupuesto(request):
    return render(request, 'Taller_mecanico/presupuesto.html')

def quienes_somos(request):
    return render(request, 'Taller_mecanico/quienes_somos.html')

def servicios(request):
    return render(request, 'Taller_mecanico/servicios.html')

def ubicacion_contacto(request):
    return render(request, 'Taller_mecanico/ubicacion_contacto.html')
