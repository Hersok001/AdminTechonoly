from django import forms 
from Empleados.models import Admin

class AdminForm(forms.ModelForm):
    
    class Meta:
        model = Admin
        fields= ['nombre','apellido','usuario','contraseña','rol','estado']

