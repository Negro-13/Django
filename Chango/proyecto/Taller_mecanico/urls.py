from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('login/', views.login_view, name='login'),
    path('administracion/', views.administracion, name='administracion'),
    path('presupuesto/', views.presupuesto, name='presupuesto'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('servicios/', views.servicios, name='servicios'),
<<<<<<< HEAD
    path('ubicacion_contacto/', views.ubicacion_contacto, name='ubicacion_contacto')
]
=======
    path('ubicacion_contacto/', views.ubicacion_contacto, name='ubicacion_contacto'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('servicios/', views.servicios, name='servicios'),
    path('servicios/crear/', views.crear_servicio, name='crear_servicio'),
    path('ficha-tecnica/', views.ficha_tecnica, name='ficha_tecnica'),
    path('ficha-tecnica/crear/', views.crear_ficha_tecnica, name='crear_ficha_tecnica'),
    path('presupuesto/', views.presupuesto, name='presupuesto'),
    path('presupuesto/crear/', views.crear_presupuesto, name='crear_presupuesto'),
    path('repuestos/', views.repuestos, name='repuestos'),
    path('proveedores/', views.proveedores, name='proveedores'),
]
>>>>>>> 106c465ed51b79ab773d7c890a85acd324f8f3fa
