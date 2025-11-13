from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import mysql.connector
import hashlib

# Configuración de la conexión MySQL
DB_CONFIG = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': '',
    'database': 'Taller_Mecanico_dj'
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def hola_mundo(request):
    return render(request, 'Taller_mecanico/hola_mundo.html')

def pagina_principal(request):
    return render(request, 'Taller_mecanico/pagina_principal.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM `Usuarios` WHERE `Usuario` = %s AND `Clave` = %s",
                (username, password)
            )
            user = cursor.fetchone()
            if user:
                request.session['user_id'] = user['Usuario']
                request.session['username'] = user['Usuario']
                messages.success(request, f'Bienvenido {username}!')
                return redirect('pagina_principal')
            else:
                messages.error(request, 'Usuario o contraseña inválidos.')
        except mysql.connector.Error as err:
            messages.error(request, f'Error de base de datos: {err}')
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
    return render(request, 'Taller_mecanico/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `Usuarios` WHERE `Usuario` = %s", (username,))
            if cursor.fetchone():
                messages.error(request, 'El usuario ya existe.')
                return redirect('register')
            cursor.execute(
                "INSERT INTO `Usuarios` (`Usuario`, `Clave`) VALUES (%s, %s)",
                (username, password)
            )
            conn.commit()
            messages.success(request, 'Registro exitoso!')
            return redirect('login')
        except mysql.connector.Error as err:
            messages.error(request, f'Error de base de datos: {err}')
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
    return render(request, 'Taller_mecanico/register.html')

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
