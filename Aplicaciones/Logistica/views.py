from django.shortcuts import render, redirect
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

def registrarProducto(request):
    codigo=request.POST['txtCode']
    nombre=request.POST['txtName']
    precio=request.POST['numPrice']
    cantidad=request.POST['numQuantity']

    producto= Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio, cantidad=cantidad)
    return redirect('/')

def edicionProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    return render(request, "editarProducto.html", {"producto": producto})

def editarProducto(request):
    codigo=request.POST['txtCode']
    nombre=request.POST['txtName']
    precio=request.POST['numPrice']
    cantidad=request.POST['numQuantity']

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.cantidad = cantidad
    producto.save()

    return redirect('/')


def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect('/')
