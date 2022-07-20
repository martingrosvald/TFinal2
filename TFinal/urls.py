"""TFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import (altaProducto, altaUsuario, listar_usuario, 
                    altaVenta, listar_ventas, buscarProducto, homepage, mostrar_stock)

urlpatterns = [
    path('', homepage, name="homepage"),
    path('home/', homepage, name="homepage"),
    path('listar_producto/', mostrar_stock, name="listado-de-producto"),
    path('admin/', admin.site.urls),
    path('agregar_producto/', altaProducto),
    #path('listar_producto/', listar_producto, name="listado-de-producto"),
    path('agregar_usuario/', altaUsuario),
    path('listar_usuario/', listar_usuario),
    path('realizar_venta/', altaVenta),
    path('listar_ventas/', listar_ventas),
    path('busqueda_producto/', buscarProducto),
]
