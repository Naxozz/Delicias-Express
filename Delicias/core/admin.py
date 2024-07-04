from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombreProducto', 'precio', 'stock']
    search_fields = ['nombreProducto']
    list_per_page = 10
    list_editable = ['precio', 'stock']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'direccion', 'telefono', 'email', 'fecha', 'producto']
    search_fields = ['rut', 'nombre', 'email']
    list_per_page = 10
    list_filter = ['fecha']

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['estado']
    search_fields = ['estado']
    list_per_page = 10
    list_filter = ['estado']