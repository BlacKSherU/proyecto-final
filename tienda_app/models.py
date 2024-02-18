from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.IntegerField(null=True, blank=True)
    imagen = models.ImageField(upload_to="tienda")
    categorias = models.ManyToManyField(Categoria)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre
