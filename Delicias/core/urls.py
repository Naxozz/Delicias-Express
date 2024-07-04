from django.urls import path, include
from .views import *

urlpatterns = [

    path('', index, name="index"),
    path('register', register, name="register"),
    path('formulario', formulario, name="formulario"),
    path('ordenes', ordenes, name="ordenes"),
    path('editar', editar, name="editar"),
]