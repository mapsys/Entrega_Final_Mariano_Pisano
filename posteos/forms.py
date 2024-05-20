from django import forms
from ckeditor.widgets import CKEditorWidget
from . import models

'''
Formulario para agregar un nuevo posteo'''
class PosteoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PosteoForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs['enctype'] = "multipart/form-data"
    class Meta:
        model = models.Posteo
        fields = "__all__"
        widgets = {
           "titulo": forms.TextInput(attrs={"class": "form-control"}),
           "subtitulo": forms.TextInput(attrs={"class": "form-control"}),
           "contenido": CKEditorWidget(), 
           "autor": forms.Select(attrs={"class": "form-control"}),
           "fecha_creacion": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
           "imagen": forms.FileInput(attrs={"class": "form-control"}),
        }

'''
Formulario que permite la busqueda de posteos'''
class FormularioBuscarPosts(forms.Form):
    titulo = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={ 'class' : 'form-control' }))