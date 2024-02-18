from django.shortcuts import render
from .models import Producto, Categoria


# Create your views here.
def home(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(
        request,
        "tienda_app/tienda_home.html",
        {"productos": productos, "categorias": categorias},
    )
