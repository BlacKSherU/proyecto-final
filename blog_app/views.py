from django.shortcuts import render
from .models import Post, Categoria


# Create your views here.
def home(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(
        request,
        "blog_app/blog_home.html",
        {
            "posts": posts,
            "categorias": categorias,
        },
    )


def categoria(request, categoria_nombre):
    categoria = Categoria.objects.get(nombre=categoria_nombre)
    posts = Post.objects.filter(categorias=categoria)
    categorias = Categoria.objects.all()
    return render(
        request,
        "blog_app/blog_categorias.html",
        {
            "posts": posts,
            "categorias": categorias,
        },
    )
