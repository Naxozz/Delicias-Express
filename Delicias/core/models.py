from django.db import models
from django.contrib.auth.models import User
    
class Producto(models.Model):  
    nombreProducto = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    

    def __str__(self):
        return self.nombreProducto
     
    
    
class Cliente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Asume que cada cliente tiene un producto
    
    def __str__(self):
        return self.rut

   
    


#class Pedido(models.Model):
 #   class EstadoChoices(models.TextChoices):
  #      PENDIENTE = 'PENDIENTE', 'Pendiente'
   #     EN_PROCESO = 'EN_PROCESO', 'En Proceso'
    #    ENVIADO = 'ENVIADO', 'Enviado'
     #   ENTREGADO = 'ENTREGADO', 'Entregado'
      #  CANCELADO = 'CANCELADO', 'Cancelado'

    #fecha = models.DateField()
    #total = models.IntegerField()
    #estado = models.CharField(max_length=50, choices=EstadoChoices.choices, default=EstadoChoices.PENDIENTE)
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    #def __str__(self):
     #   return str(self.id)