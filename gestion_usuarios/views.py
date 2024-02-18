from urllib.request import Request
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
class Registro(View):
    def get(self, request):
        mi_formulario = UserCreationForm()
        return render(
            request, "gestion_usuarios/registro.html", {"mi_formulario": mi_formulario}
        )

    def post(self, request):
        mi_formulario = UserCreationForm(request.POST)
        if mi_formulario.is_valid():
            usuario = mi_formulario.save()
            login(request, usuario)
            return redirect("home")
        else:
            for msg in mi_formulario.error_messages:
                messages.error(request, mi_formulario.error_messages[msg])
            return render(
                request,
                "gestion_usuarios/registro.html",
                {"mi_formulario": mi_formulario},
            )


def cerrar_sesion(request):
    logout(request)
    return redirect("home")


class iniciar_sesion(View):
    def get(self, request):
        mi_formulario = AuthenticationForm()
        return render(
            request,
            "gestion_usuarios/iniciar_sesion.html",
            {"mi_formulario": mi_formulario},
        )

    def post(self, request):
        mi_formulario = AuthenticationForm(request, data=request.POST)
        if mi_formulario.is_valid():
            nombre_usuario = mi_formulario.cleaned_data.get("username")
            contraseña_usuario = mi_formulario.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contraseña_usuario)
            login(request, usuario)
            return redirect("home")
        else:
            for msg in mi_formulario.error_messages:
                messages.error(request, mi_formulario.error_messages[msg])
            return render(
                request,
                "gestion_usuarios/registro.html",
                {"mi_formulario": mi_formulario},
            )
