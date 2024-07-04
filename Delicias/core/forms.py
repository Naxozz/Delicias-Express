from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['idFactura','rut', 'nombre', 'direccion', 'telefono', 'email', 'producto', 'estadoFactura']
        labels = {
            'idFactura': 'ID Orden',
            'rut': 'RUT',
            'nombre': 'Nombre',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Correo',
            'producto': 'Producto',
            'estadoFactura': 'Estado'
        }
        widgets = {
            'idFactura': forms.TextInput(attrs={'placeholder': 'Ingrese ID de la orden'}),
            'rut': forms.TextInput(attrs={'placeholder': 'Ingrese RUT del cliente sin puntos ni guión ej: 207435420'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre cliente'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingrese dirección ej: Las Loicas 1283'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese número de teléfono'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese correo electrónico ej: Tulio@gmail.com'}),
            'producto': forms.Select(attrs={'placeholder': 'Seleccione un producto'}),
        }

class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')