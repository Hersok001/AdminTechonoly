from django.db import models

class venta(models.Model):
    
    nombre_productos=models.CharField(max_length=50)
    cantidad_venta_producto=models.IntegerField()
    precio_total=models.BigIntegerField()
    
    class Meta:
        verbose_name='venta'
        verbose_name_plural='ventas'
    
    

   
