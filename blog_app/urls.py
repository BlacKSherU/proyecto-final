from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog"),
    path("<str:categoria_nombre>/", views.categoria, name="categoria"),
]
