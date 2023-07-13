# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home)
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarProducto/', views.registrarProducto),
    path('edicionProducto/<codigo>', views.edicionProducto),
    path('editarProducto/', views.editarProducto),
    path('eliminarProducto/<codigo>', views.eliminarProducto)
]