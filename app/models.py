from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField


# Create your models here.

class Usuario(models.Model):
    #t_usuario = (
    #    ("1", "Administrador"),
    #    ("2", "Cliente")
    #    )
    #tipo_de_usuario = models.CharField(
    #    max_length = 20,
    #    choices = t_usuario, 
    #    default = "1"
    #    )
    tipo_de_usuario=models.CharField(max_length=40)
    clave =  models.CharField(max_length=40)
    apellido_nombre =  models.CharField(max_length=80)
    correo_elec = models.EmailField(max_length=90)
    nro_celular = models.IntegerField()
    direccion = models.CharField(max_length=200)
    #pais = CountryField()

class Producto(models.Model):
    id_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=40)
    #opciones_cat_productos=(
    #    ("1", "Textil"), 
    #    ("2", "Elementos de pesca"),
    #    ("3", "Accesorios")
    #        )
    #categoria_producto = models.CharField(
    #    max_length=20,
    #    choices=opciones_cat_productos, 
    #    default="1")
    categoria_producto=models.CharField(max_length=40)
    marca_producto = models.CharField(max_length=40)
    descripcion_producto= RichTextField()
    precio = models.IntegerField()
    cantidad_disponible = models.IntegerField()
    #fotos_productos= models.ImageField(upload_to="productos", null=True, blank=True)
    #responsable_carga = models.CharField(max_length=40)
    fecha_creacion_producto = models.DateField()
    #fecha_actualiz = models.DateField() 

class Ventas(models.Model):
    id_venta = models.IntegerField()
    fecha_venta = models.DateField()
    id_producto = models.IntegerField()
    cantidad_producto= models.IntegerField()
    valor_total= models.IntegerField()
    #usuario_transaccion = 
    

#class Historial_stock(models.Model):
#    fecha_movimiento = models.Datefield()
#    id_producto_movimiento = models.CharField(max_length=40)
#    responsable_movimiento = models.CharField(max_length=40)
#    tipo_mov = 
#    #cantidad = poner el cambio en la cantidad del producto
#    pass