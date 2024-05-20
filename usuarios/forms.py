from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserChangeForm


'''
Form para Login
'''
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = models.User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

'''
Form de creacion de usuarios'''
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar password', widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, required=False, help_text='')
    last_name = forms.CharField(max_length=30, required=False, help_text='')

    
    class Meta:
        model = models.User
        fields = ["username", "password1", "password2", "email", "first_name", "last_name"]
        help_texts = {k:'' for k in fields}


class UserExtended(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ["email", "first_name", "last_name"]



'''
Formulario para edicion de perfil'''
class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(required=True)
    last_name = forms.CharField(max_length=30, required=False, help_text='')
    first_name = forms.CharField(max_length=30, required=False, help_text='')

    class Meta:
        model = models.User
        fields = ["email", "first_name", "last_name"]