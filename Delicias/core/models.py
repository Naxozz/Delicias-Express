from django.db import models
from django.contrib.auth.models import User
    
class Producto(models.Model):  
    nombreProducto = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    

    def __str__(self):
        return self.nombreProducto
     
class Factura(models.Model):
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado
    
class Cliente(models.Model):
    idFactura = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Asume que cada cliente tiene un producto
    estadoFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)  # Asume que cada cliente tiene una factura

    def __str__(self):
        return self.rut




