from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label=_("Nombre de usuario:"),
    )

    email = forms.EmailField(
        label=_("Email:"),
    )
    
    first_name = forms.CharField(
        label=_("Nombre:"),
    )
    
    last_name = forms.CharField(
        label=_("Apellido:"),

    )
    
    dni = forms.CharField(
        label=_("DNI")
    )

    password1 = forms.CharField(
        label=_("Contraseña:"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
   
    password2 = forms.CharField(
        label=_("Confirmar contraseña:"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'dni', 'email', 'password1', 'password2']


