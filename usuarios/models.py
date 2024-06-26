from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
Modelo extendido de User para poder agregarle un avatar y una descripcion'''
class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    def __str__(self) -> str:
        return f'{self.user} - {self.avatar}'