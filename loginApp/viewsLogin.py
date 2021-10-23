from django.core.checks import messages
from django.db import models
from Empleados.models import Admin
from django.shortcuts import redirect, render
from django.http.response import HttpResponseGone
from django.shortcuts import render, HttpResponse





# Create your models here.
#metodo para comprobar que el usuario existe en la base de datos y logear



def Index(request):
    return render(request,'loginApp/index.html')




