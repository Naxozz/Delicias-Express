from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def register(request):
    
    data ={
        'form' : RegistroUsuarioForm()
    }
    
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            #login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        data ["form"] = formulario

    return render(request, 'registration/register.html', data)

def formulario(request):
    
    data={
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
            
        else:
            data['form'] = formulario 
    return render(request, 'core/formulario.html', data)


def ordenes(request):
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()

    # Calcular el precio total de todos los productos
    total_final = 0

    for producto in productos:
        total_final += producto.precio * producto.stock

    # Calcular el IVA del 19% sobre el total_final
    totalIva = round(total_final * 0.19)

    # Agregar total_final y total_iva a la lista de productos
    lista_productos = []
    for producto in productos:
        producto.total_final = producto.precio * producto.stock
        lista_productos.append(producto)

    data = {
        'listaFacturas': clientes,
        'listaProductos': lista_productos,
        'total_final': total_final,
        'totalIva': totalIva,
    }

    return render(request, 'core/ordenes.html', data)

