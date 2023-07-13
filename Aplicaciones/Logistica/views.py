from django.shortcuts import render
from .models import Producto

# # Create your views here.

# def home(request):
#     productosListados = Producto.objects.all()
#     return render(request, "gestionProductos.html", {"productos": productosListados})

def home(request):
    search_query = request.GET.get('search_query', '')  # Obtener el término de búsqueda de request.GET

    if search_query:
        productosListados = Producto.objects.filter(nombre__icontains=search_query)
    else:
        productosListados = Producto.objects.all()
    
    return render(request, "gestionProductos.html", {"productos": productosListados})