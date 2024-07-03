from django.contrib import admin
from .models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombreProducto', 'precio', 'stock']
    search_fields = ['nombreProducto']
    list_per_page = 10
    list_editable = [ 'precio','stock']
   

admin.site.register(Producto, ProductoAdmin)    