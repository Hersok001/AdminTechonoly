from django.shortcuts import redirect, render
from InventariosApp.models.Inventario import inventario
from InventariosApp.forms import InventarioForm

# Create your views here.

#Metodos y views

def Inventario(request):
    Inventarios=inventario.objects.all()
    context= {'inventarios':Inventarios}
    return render(request, 'InventariosApp/inventario.html', context)

#metodo agregar
def agregarInv(request):
    if request.method == "POST":
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inventario")
    else:
        form=InventarioForm()
    context={'form':form}
    return render(request, 'InventariosApp/agregarInventario.html', context)

#Metodo eliminar
def eliminarInv(request, id):
    eliminar = inventario.objects.get(id=id)
    eliminar.delete()
    return redirect("inventario")

#Metodo modificar 
def modificarInv(request, id):
    modificar = inventario.objects.get(id=id)
    if request.method == "POST":
        form= InventarioForm(request.POST, instance=modificar)
        if form.is_valid():
            form.save()
            return redirect("inventario")  
    else:
        form= InventarioForm(instance=modificar)        
    context={'form':form}
    return render(request, 'InventariosApp/modificarInv.html', context)