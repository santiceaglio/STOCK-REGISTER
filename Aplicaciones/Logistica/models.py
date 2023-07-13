from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    cantidad = models.PositiveSmallIntegerField()
    # precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio = models.CharField(max_length=15, default='0')

    

    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super().save(*args, **kwargs)


    def __str__(self):
        texto = '{0} ({1})'
        return texto.format(self.nombre, self.cantidad)
    
    # def save(self, *args, **kwargs):
    #     self.precio = self.cantidad * 10  # Multiplica el campo cantidad por un factor (en este caso, 10)
    #     super().save(*args, **kwargs)