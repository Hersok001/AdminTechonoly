# Generated by Django 3.2.7 on 2021-10-21 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0002_remove_venta_nombre_comprador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='nombre_producto',
            new_name='nombre_productos',
        ),
    ]
