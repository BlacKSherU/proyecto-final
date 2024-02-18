from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="tienda"),
    path("", include("carro.urls")),
    path("", include("pedidos.urls")),
]
