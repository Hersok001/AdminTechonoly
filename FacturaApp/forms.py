from django import forms 
from FacturaApp.models.facturacion import venta

class VentaForm(forms.ModelForm):
    
    class Meta:
        model = venta
        fields= ['nombre_productos','cantidad_venta_producto','precio_total']