from django import forms
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Agregar_Usuario (forms.Form):
    #t_usuario = (
    #    ("1", "Administrador"),
    #    ("2", "Cliente")
    #    )
    #tipo_de_usuario = forms.CharField(
    #    max_length = 20,
    #    choices = t_usuario, 
    #    default = "1"
    #    )
    tipo_de_usuario = forms.CharField(max_length=40)
    clave =  forms.CharField(max_length=40)
    apellido_nombre =  forms.CharField(max_length=80)
    correo_elec = forms.EmailField(max_length=90)
    nro_celular = forms.IntegerField()
    direccion = forms.CharField(max_length=200)

class Agregar_Producto (forms.Form):
    id_producto = forms.IntegerField()
    nombre_producto = forms.CharField(max_length=40)
    #opciones_cat_productos=(
    #    ("1", "Textil"), 
    #    ("2", "Elementos de pesca"),
    #    ("3", "Accesorios")
    #        )
    #categoria_producto = forms.CharField(
    #    max_length=20,
    #    choices=opciones_cat_productos, 
    #    default="1")
    categoria_producto = forms.CharField(max_length=40)
    marca_producto = forms.CharField(max_length=40)
    descripcion_producto= RichTextField()
    precio = forms.IntegerField()
    cantidad_disponible = forms.IntegerField()
    fecha_creacion_producto = forms.DateField()

class Realizar_venta (forms.Form):
    id_venta = forms.IntegerField()
    fecha_venta = forms.DateField()
    id_producto = forms.IntegerField()
    cantidad_producto= forms.IntegerField()
    valor_total= forms.IntegerField()

class Busqueda_Producto (forms.Form):
    criterio = forms.CharField(max_length=40)