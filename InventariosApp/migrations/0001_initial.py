# Generated by Django 3.2.8 on 2021-10-14 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=50)),
                ('cantidad_inventario', models.IntegerField()),
                ('descripcion_producto', models.CharField(max_length=150)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]