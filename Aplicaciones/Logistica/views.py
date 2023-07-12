from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    productosListados = Producto.objects.all()
    return render(request, "gestionProductos.html", {"productos": productosListados})