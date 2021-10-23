from django.shortcuts import redirect, render
from Empleados.models import Admin
from Empleados.forms import AdminForm


# Create your views here

def admin(request):
    admins=Admin.objects.all()
    context= {'admins':admins}
    return render(request, 'authApp/administrador.html', context)

#metodo agregar
def agregar(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("administrador")
    else:
        form=AdminForm()
    context={'form':form}
    return render(request, 'authApp/agregarAdmin.html', context)

#Metodo eliminar
def eliminar(request, id):
    eliminar = Admin.objects.get(id=id)
    eliminar.delete()
    return redirect("administrador")

#Metodo modificar 
def modificar(request, id):
    modificar = Admin.objects.get(id=id)
    if request.method == "POST":
        form= AdminForm(request.POST, instance=modificar)
        if form.is_valid():
            form.save()
            return redirect("administrador")  
    else:
        form= AdminForm(instance=modificar)        
    context={'form':form}
    return render(request, 'authApp/modificar.html', context)
