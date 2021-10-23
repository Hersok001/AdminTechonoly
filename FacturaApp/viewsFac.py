from django.shortcuts import render
from django.shortcuts import redirect


from InventariosApp.models.Inventario import inventario
from FacturaApp.forms import VentaForm


# Create your views here.

#views de la tablas
def InventarioFac(request):
    Inventarios=inventario.objects.all()
    context= {'inventarios':Inventarios}
    return render(request, 'FacturaApp/factura.html', context)



def agregarVenta(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("factura")
    else:
        form=VentaForm()
    context={'form':form}
    return render(request, 'FacturaApp/factura.html', context)





