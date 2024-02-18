from django.urls import path
from . import views

urlpatterns = [
    path("registro", views.Registro.as_view(), name="registro"),
    path("cerrar_sesion", views.cerrar_sesion, name="cerrar_sesion"),
    path("iniciar_sesion", views.iniciar_sesion.as_view(), name="iniciar_sesion"),
]
