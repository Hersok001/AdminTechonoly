# Generated by Django 3.2.8 on 2021-10-15 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventariosApp', '0002_auto_20211015_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='precio',
            field=models.BigIntegerField(),
        ),
    ]
