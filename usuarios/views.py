from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomAuthenticationForm, CustomUserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from . import models, forms
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserExtended
from django.contrib.auth import login


# # Create your views here.
# class CustomLoginView(LoginView):
#     authentication_form = CustomAuthenticationForm
#     template_name = "usuarios/login.html"


def iniciar_sesion(request):

# Sólo permite el ingreso si NO se está logueado. Caso contrario, redirige a 'home'
# Esta validación es útil cuando se intenta ingresar forzando la URL
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        formulario_login = AuthenticationForm(request, data=request.POST)
        if formulario_login.is_valid():
            user = formulario_login.get_user()
            login(request, user)
            user_extension, es_nuevo_userextension = UserExtended.objects.get_or_create(user=request.user)
            return redirect('core:home')
    else:
        formulario_login = AuthenticationForm()

    return render(request, 'usuarios/login.html', { 'form' : formulario_login })

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/index.html", {"mensaje": "Usuario creado"})
    else:
        form = CustomUserCreationForm()
    return render(request, "usuarios/register.html", {"form": form})

@login_required
def ver_perfil(request):
    return render(request, 'usuarios/ver_perfil.html')

# @login_required
# def userextended_update(request, pk: int):
#     query = models.User.objects.get(id=pk)
#     if request.method == "POST":
#         form = forms.UserExtended(request.POST, instance=query)
#         if form.is_valid:
#             form.save()
#             return redirect("usuarios:ver_perfil")
#     else:  # request.method == "GET"
#         form = forms.UserExtended(instance=query)
#     return render(request, "usuarios/editar_perfil.html", context={"form": form})


@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = forms.UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            # usuario.password1 = informacion['password1']
            # usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "usuarios/ver_perfil.html")

    else:

        miFormulario = forms.UserEditForm(initial={'email': usuario.email, 'last_name': usuario.last_name, 'first_name': usuario.first_name})

    return render(request, "usuarios/editar_perfil.html", {"form": miFormulario, "usuario": usuario})

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name="usuarios/cambiar_password.html"
    success_url = reverse_lazy("usuarios:ver_perfil")