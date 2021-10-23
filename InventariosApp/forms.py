from django import forms 
from InventariosApp.models.Inventario import inventario

class InventarioForm(forms.ModelForm):
    
    class Meta:
        model = inventario
        fields= ['nombre_producto','cantidad_inventario','descripcion_producto','precio']