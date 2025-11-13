from django import forms
from .models import Servicio, FichaTecnica, Presupuesto, Repuesto, Proveedor

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio_base']

class FichaTecnicaForm(forms.ModelForm):
    class Meta:
        model = FichaTecnica
        fields = ['cod_cliente', 'vehiculo', 'subtotal', 'mano_obra', 'total_general']

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ['cod_cliente', 'descripcion', 'total_presupuesto', 'total_gastado']

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ['cod_repuesto', 'descripcion', 'precio_unitario', 'proveedor']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['cod_proveedor', 'nombre', 'direccion', 'telefono', 'email']
