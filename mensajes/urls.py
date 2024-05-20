from django.urls import path, include
from . import views

app_name = "mensajes"



urlpatterns = [
    path("", views.mensajes_list, name="home"),
    path("ver_intercambio/<int:intercambio_id>/", views.detalle_conversacion, name="detalle_conversacion"),
    path("nuevo_mensaje/<int:intercambio_id>/", views.nuevo_mensaje, name="nuevo_mensaje"),
    path('iniciar-conversacion/', views.iniciar_conversacion, name='iniciar_conversacion'),
]