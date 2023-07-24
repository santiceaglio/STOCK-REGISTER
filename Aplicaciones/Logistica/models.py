# from django.db import models
# from decimal import Decimal

# # Create your models here.

# class Producto(models.Model):
#     codigo = models.CharField(primary_key=True, max_length=6)
#     nombre = models.CharField(max_length=50)
#     cantidad = models.PositiveSmallIntegerField()
#     precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     # precio = models.CharField(max_length=15, default='0')
    
#     def clean(self):
#         # Procesar el valor ingresado por el usuario en el campo precio
#         # y convertirlo a un número decimal antes de la validación del modelo
#         try:
#             self.precio = Decimal(self.precio)
#         except (TypeError, ValueError):
#             raise models.ValidationError('El valor de “{}” debe ser un número decimal.'.format(self.precio))

           

    

    


# def __str__(self):
#         texto = '{0} ({1})'
#         return texto.format(self.nombre, self.cantidad)
    
from django.db import models
from decimal import Decimal

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    cantidad = models.PositiveSmallIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Procesar el valor ingresado por el usuario en el campo precio
        # y convertirlo a un número decimal antes de guardar el objeto en la base de datos
        if isinstance(self.precio, str):  # Verificar si el valor es una cadena (str)
            # Eliminar símbolos no numéricos del valor (por ejemplo, "$" y ".")
            precio_numerico = Decimal(self.precio.replace("$", "").replace(",", ""))
            self.precio = precio_numerico

        super().save(*args, **kwargs)

    def __str__(self):
        texto = '{0} ({1})'
        return texto.format(self.nombre, self.cantidad)