"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from django.urls import path,include
from django.contrib.auth import views as auth_views

from authApp import views

from Empleados import viewsEmp

from InventariosApp import viewsInventario

from FacturaApp import viewsFac
from FacturaApp import viewsCarr

from loginApp import viewsLogin


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    #App Administrador
    path('administrador/', viewsEmp.admin, name="administrador"),    
    path('administrador/agregar/', viewsEmp.agregar, name="agregar"),
    path('administrador/eliminar/<int:id>/', viewsEmp.eliminar, name="eliminar"),
    path('administrador/editar/<int:id>/', viewsEmp.modificar, name="modificar"),
     #App Inventarios
    path('inventarios/', viewsInventario.Inventario, name="inventario"),
    path('inventarios/agregar/', viewsInventario.agregarInv, name="agregarInv"),
    path('inventarios/eliminar/<int:id>/', viewsInventario.eliminarInv, name="eliminarInv"),
    path('inventarios/modificar/<int:id>/', viewsInventario.modificarInv, name="modificarInv"),
    #App facturas
    path('facturas/', viewsFac.InventarioFac, name="factura"),
    path("agregar/<int:inventario_id>/", viewsCarr.agregar_producto, name="agregarCarrito"),
    path("eliminar/<int:inventario_id>/", viewsCarr.eliminar_producto, name="eliminarCarrito"),
    path("restar/<int:inventario_id>/", viewsCarr.restar_producto, name="restarCarrito"),
    path("limpiar/", viewsCarr.limpiar_carro, name="limpiarCarrito"),
    #Login
    path('', viewsLogin.Index, name="home"),
    

]



