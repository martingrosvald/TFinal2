from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from app.forms import Agregar_Producto, Agregar_Usuario, Realizar_venta, Busqueda_Producto
from app.models import Producto, Usuario, Ventas
from ckeditor.fields import RichTextField
# Create your views here.

def homepage(request):
    return render(request, "app/index.html", {})

def mostrar_stock(request):
    context= {}
    
    context["producto"] = Producto.objects.all()
    return render(request, "app/listado_producto.html", context)


def altaProducto(request):
    if request.method == 'POST':
        agregar_producto = Agregar_Producto(request.POST)
        
        if agregar_producto.is_valid():
            informacion = agregar_producto.cleaned_data
            producto = Producto(id_producto=informacion["id_producto"], nombre_producto=informacion["nombre_producto"], categoria_producto=informacion["categoria_producto"],marca_producto=informacion["marca_producto"],precio=informacion["precio"],cantidad_disponible=informacion["cantidad_disponible"],fecha_creacion_producto=informacion["fecha_creacion_producto"])
            producto.save()
        return redirect(reverse_lazy("listar-producto"))
    
    else:
        agregar_producto= Agregar_Producto()
    return render (request,"app/agregar_producto.html",{"agregar_producto":agregar_producto})

#def listar_producto(request):
#    context= {}
#    
#    context["producto"] = Producto.objects.all()
#    return render(request, "app/listado_producto.html", context)


def altaUsuario(request):
    if request.method == 'POST':
        agregar_usuario = Agregar_Usuario(request.POST)
        
        if agregar_usuario.is_valid():
            informacionu = agregar_usuario.cleaned_data
            usuario = Usuario(tipo_de_usuario=informacionu["tipo_de_usuario"], clave=informacionu["clave"], apellido_nombre=informacionu["apellido_nombre"],correo_elec=informacionu["correo_elec"],nro_celular=informacionu["nro_celular"],direccion=informacionu["direccion"])
            usuario.save()
        return render (request, "app/listado_usuario.html")
    
    else:
        agregar_usuario= Agregar_Usuario()
    return render (request,"app/agregar_usuario.html",{"agregar_usuario":agregar_usuario})

def listar_usuario(request):
    context= {}
    
    context["usuario"] = Usuario.objects.all()
    return render(request, "app/listado_usuario.html", context)

def altaVenta(request):
    if request.method == 'POST':
        realizar_venta = Realizar_venta(request.POST)
        
        if realizar_venta.is_valid():
            informacionv = realizar_venta.cleaned_data
            venta = Ventas(id_venta=informacionv["id_venta"], fecha_venta=informacionv["fecha_venta"], id_producto=informacionv["id_producto"],cantidad_producto=informacionv["cantidad_producto"],valor_total=informacionv["valor_total"])
            venta.save()
        return render (request, "app/listado_ventas.html")
    
    else:
        realizar_venta= Realizar_venta()
    return render (request,"app/realizar_venta.html",{"realizar_venta":realizar_venta})

def listar_ventas(request):
    context= {}
    
    context["venta"] = Ventas.objects.all()
    return render(request, "app/listado_ventas.html", context)

#def busqueda_producto(request):
#   return render(request,"app/busqueda_producto.html")

def buscarProducto(request):
    
    formulario_busqueda = Busqueda_Producto()
    
    if request.GET:
        formulario_busqueda = Busqueda_Producto(request.GET)
        if formulario_busqueda.is_valid():
            productos = Producto.objects.filter(nombre_producto=formulario_busqueda.cleaned_data["criterio"]).all()
            return render(request, "app/busqueda_producto.html", {"productos": productos})
    
    return render(request, "app/busqueda_producto.html", {"formulario_busqueda":formulario_busqueda})
