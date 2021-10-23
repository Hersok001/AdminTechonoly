from django.db import models

class inventario(models.Model):
    nombre_producto=models.CharField(max_length=50)
    cantidad_inventario=models.IntegerField()
    descripcion_producto=models.CharField(max_length=150)
    precio=models.BigIntegerField()

    

    class Meta:
        verbose_name='inventario'
        verbose_name_plural='inventarios'
    

    