from FacturaApp.serializers.Carrito import Carro
from django.shortcuts import render
from django.shortcuts import redirect
from InventariosApp.models.Inventario import inventario


#Views del carrito

def agregar_producto(request, inventario_id):
    
    carro=Carro(request)

    producto=inventario.objects.get(id=inventario_id)

    carro.agregar(inventario=producto)

    return redirect("factura")


def eliminar_producto(request, inventario_id):
    
    carro=Carro(request)

    producto=inventario.objects.get(id=inventario_id)

    carro.eliminar(inventario=producto)

    return redirect("factura")


def restar_producto(request, inventario_id):
    
    carro=Carro(request)

    producto=inventario.objects.get(id=inventario_id)

    carro.restar_inventario(inventario=producto)

    return redirect("factura")

def limpiar_carro(request):
    
    carro=Carro(request)

    carro.limpiar()

    return redirect("factura")