from django.db import models
from ckeditor.fields import RichTextField 
from django.contrib.auth.models import User

# Create your models here.
'''
Modelo de posts
'''
class Posteo(models.Model):

    titulo         = models.CharField(max_length=255)
    subtitulo      = models.CharField(max_length=255)
    contenido      = RichTextField(null=True)
    autor          = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True, auto_now=False)
    imagen         = models.ImageField(upload_to='galeria', null=True, blank=True)