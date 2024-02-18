from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .forms import FormularioContacto


# Create your views here.
def contacto(request):
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            print(email)
            contenido = request.POST.get("contenido")
            try:
                send_mail(
                    "contacto %s gestion pedidos BlacKSherU Store" % nombre,
                    "%s \ncontacta a %s a traves del correo %s "
                    % (contenido, nombre, email),
                    "blacksheru@gmail.com",
                    [
                        "tramitesgarciamiguel@gmail.com",
                    ],
                )
                return redirect("./?valido")
            except:
                return redirect("./?novalido")

    formulario_contacto = FormularioContacto()
    return render(
        request, "contacto_app/contacto.html", {"mi_formulario": formulario_contacto}
    )
