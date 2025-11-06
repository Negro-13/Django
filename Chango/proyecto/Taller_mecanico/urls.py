from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola_mundo, name='hola_mundo'),
    path('login/', views.login, name='login'),
    path('administracion/', views.administracion, name='administracion'),
    path('presupuesto/', views.presupuesto, name='presupuesto'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('servicios/', views.servicios, name='servicios'),
    path('ubicacion_contacto/', views.ubicacion_contacto, name='ubicacion_contacto'),
]
