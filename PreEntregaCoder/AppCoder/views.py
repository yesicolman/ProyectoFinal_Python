from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):

    return render(request, 'AppCoder/inicio.html')

<<<<<<< HEAD
def productos(request):

    return render(request, 'AppCoder/productos.html')
=======

def Productos(request):

    return render(request, 'AppCoder/Productos.html')
>>>>>>> e59efd4366abba8b1c91e9a6199c475f84f6c502
