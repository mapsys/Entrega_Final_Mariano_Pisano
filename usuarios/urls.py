from django.urls import include, path
from django.contrib.auth.views import LogoutView
from . import views
app_name = "usuarios"


urlpatterns = [
    path("login/", views.iniciar_sesion, name="login"),
    path("logout/", LogoutView.as_view(template_name="usuarios/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("ver_perfil/", views.ver_perfil, name="ver_perfil"),
    path("editar_perfil/", views.editarPerfil, name="editar_perfil"),
    path("cambia_password/", views.CambiarPassword.as_view(), name="cambiar_password"),
]
