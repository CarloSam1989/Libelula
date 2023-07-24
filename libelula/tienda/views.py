from .models import *
from django.views.generic import ListView
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProductoForm, UserRegisterForm, CategoriaForm, BusquedaForm
from django.contrib import messages
from .models import Producto
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'tienda/index.html')

def ver_productode(request, id):
    producto=Producto.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def registrar(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            form.save()
            messages.success(request, f'Usuario {usuario} creado')
            return redirect(index)
    else:
        form = UserRegisterForm()
    contex = { 'form':form}
    return render(request, 'tienda/register.html', contex)

def view_producto(request):
    return render(request, 'tienda/productos.html',{
        "producto":Producto.objects.all()
    })

def add(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_producto = form.cleaned_data['nombre']
            nuevo_precio = form.cleaned_data['precio']
            nuevo_categoria = form.cleaned_data['categoria']
            nueva_cantidad=form.cleaned_data['cantidad_disponible']
            nueva_descripcion=form.cleaned_data['descripcion']
            nueva_imagen=form.cleaned_data['imagen']
            nuevoproducto = Producto(
                nombre = nuevo_producto,
                precio = nuevo_precio,
                categoria = nuevo_categoria,
                cantidad_disponible = nueva_cantidad,
                descripcion = nueva_descripcion,
                imagen=nueva_imagen,
            )
            nuevoproducto.save()
            return render(request, 'tienda/registrar_producto.html',{
                'form':ProductoForm(),
                'success':True
            })
    else:
        form = ProductoForm()
        return render(request,'tienda/registrar_producto.html',{
           'form':ProductoForm(),
        })
    
def addcategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            nuevo_producto = form.cleaned_data['nombre']
            nueva_descripcion=form.cleaned_data['descripcion']
            nuevoproducto = Categoria(
                nombre = nuevo_producto,
                descripcion = nueva_descripcion,
            )
            nuevoproducto.save()
            messages.success(request, f'Producto {nuevo_producto} registrado')
            return redirect(index)
    else:
        form = CategoriaForm()
        return render(request,'tienda/registrar_categoria.html',{
           'form':CategoriaForm()
        })
    
def edita(request, id):
    if request.method == 'POST':
        producto = Producto.objects.get(pk=id)
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return render(request, 'inventario/edit.html', {
                'form':form,
                'success':True
            })
    else:
        producto=Producto.objects.get(pk=id)
        form = ProductoForm(instance=producto)
        
    return render(request, 'inventario/edit.html', {
        'form':form
    })

def elimina(request, id):
    if request.method == 'POST':
        producto = Producto.objects.get(pk=id)
        producto.estado='I'
        producto.save()
    return HttpResponseRedirect(reverse('index'))

def listar_productos(request):
    productos = list(Producto.objects.values())
    data = {'productos':productos}
    return JsonResponse(data)

def buscar_productos(request):
    productos = Producto.objects.all()
    form = BusquedaForm(request.GET)
    if form.is_valid():
        terminos_busqueda = form.cleaned_data['terminos_busqueda']
        if terminos_busqueda:
            productos = productos.filter(nombre__icontains=terminos_busqueda)

    return render(request, 'buscar.html', {'form': form, 'productos': productos})

