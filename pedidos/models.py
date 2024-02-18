from django.db import models
from django.contrib.auth.models import User
from tienda_app.models import Producto
from django.db.models import F, Sum, FloatField


# Create your models here.
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"

    @property
    def total(self):
        return self.LineaPedido_set.agregate(
            total=Sum(F("precio") * F("cantidad"), output_field=FloatField())
        )["total"]

    def __str__(self):
        return str(self.id)


class LineaPedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "linea_pedido"
        verbose_name_plural = "linea_pedidos"

    def __str__(self):
        return f"{self.cantidad} unidades de {self.producto.nombre}"
