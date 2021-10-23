from django.db import models

# Create your models here.

from django.db import models

class Admin(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    usuario=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=50)
    rol=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
     

    def __str__(self):
        return self.nombre
    
class Meta:
    verbose_name='admin'
    verbose_name_plural='admin'
