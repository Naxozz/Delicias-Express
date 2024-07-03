from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test



def grupo_requerido(nombre_grupo):
    def decorator(view_fuc):
        @user_passes_test(lambda user: user.groups.filter(name=nombre_grupo).exists())
        def wrapper(request, *args, **kwargs):
            return view_fuc(request, *args, **kwargs)
        return wrapper
    return decorator
# @grupo_requerido('admin')






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
            #messages.success(request, "Te has registrado correctamente")
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
    facturas = Factura.objects.all()  # Obtener todas las facturas

    # Calcular el precio total de todos los productos
    total_final = 0
    

    for producto in productos:
        total_final = producto.precio * producto.stock

    # Calcular el IVA del 19% sobre el total_final
    totalIva = total_final * 0.19

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
    if request.method == 'POST':
        # Obtener el ID de la factura a aceptar o rechazar desde el formulario
        factura_id = request.POST.get('factura_id')

        if 'aceptar_factura' in request.POST:
            factura = get_object_or_404(Factura, id=factura_id)
            factura.aceptar_factura()
            messages.success(request, f"Factura {factura_id} aceptada correctamente.")
            return redirect(reverse('ordenes'))

        elif 'rechazar_factura' in request.POST:
            motivo_rechazo = request.POST.get('motivo_rechazo', '')
            factura = get_object_or_404(Factura, id=factura_id)
            factura.rechazar_factura(motivo=motivo_rechazo)
            messages.success(request, f"Factura {factura_id} rechazada correctamente.")
            return redirect(reverse('ordenes'))

    return render(request, 'core/ordenes.html', data)

