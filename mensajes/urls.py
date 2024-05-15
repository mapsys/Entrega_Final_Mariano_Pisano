from django.urls import path, include
from . import views

app_name = "mensajes"



urlpatterns = [
    path("", views.mensajes_list, name="home"),
    path("ver_intercambio/<int:intercambio_id>/", views.detalle_conversacion, name="detalle_conversacion"),
]