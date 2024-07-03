from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class RegistroUsuarioForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        