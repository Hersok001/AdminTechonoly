# Generated by Django 3.2.8 on 2021-10-15 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventariosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventario',
            options={'verbose_name': 'inventario', 'verbose_name_plural': 'inventarios'},
        ),
        migrations.AlterField(
            model_name='inventario',
            name='precio',
            field=models.FloatField(),
        ),
    ]
