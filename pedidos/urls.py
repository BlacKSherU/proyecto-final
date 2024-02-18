from django.urls import path, include
from . import views

urlpatterns = [
    path("procesar_pedido", views.procesar_pedido, name="procesar_pedido"),
]
