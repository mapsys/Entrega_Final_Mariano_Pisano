from django.db import models
from django.contrib.auth.models import User

'''
Modelo para intercambio de mensajes
Tenemos una clase principal que es Intercambio
que contiene la configuracion del intercambio
y despues la clase mensajes que mantiene cada mensaje perteneciente a un intercambio
'''
class Intercambio(models.Model):

    user_1    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_1')
    user_2    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_2')
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

class Mensaje(models.Model):

    chat       = models.ForeignKey(Intercambio, on_delete=models.CASCADE)
    de_user    = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mensaje  = models.CharField(max_length=255)
    fecha_hora_enviado = models.DateTimeField(auto_now_add=True, auto_now=False)
    leido = models.BooleanField(default=False)
    fecha_hora_leido = models.DateTimeField(null=True, blank=True)
