from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

from blog.models import Usuario, Post, Avatar

class PostFormulario(forms.Form):
    categoria = forms.CharField(max_length=255)
    titulo = forms.CharField(max_length=255)
    intro = forms.CharField()
    texto = forms.CharField()
    autor = forms.CharField(max_length=255)
    fecha_publicacion = forms.DateTimeField()
    imagen = forms.ImageField()
    


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'dni', 'email',]



class UserRegisterForm(UserCreationForm):
    # Esto es un ModelForm
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']



class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']
