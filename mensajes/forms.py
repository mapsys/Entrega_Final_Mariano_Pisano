from django import forms
from django.contrib.auth.models import User

'''
Formulario para creacion de nuevo intercambio de mensajes
'''
class NuevoIntercambioForm(forms.Form):
    user_id = forms.ModelChoiceField(
        queryset=User.objects.none(),
        label='Selecciona un usuario',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_id'].queryset = User.objects.exclude(id=user.id)
