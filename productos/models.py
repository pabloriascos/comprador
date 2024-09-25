from django.db import models

# Create your models here.
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Fuente(models.Model):
    nombre = models.CharField(max_length=100)
    api_key = models.CharField(max_length=255, blank=True, null=True)
    url_base = models.URLField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Precio(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fuente = models.ForeignKey(Fuente, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    url_compra = models.URLField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.producto.nombre} - {self.fuente.nombre}"
