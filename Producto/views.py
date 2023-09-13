from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from django.http import HttpResponse
from cliente.models import Proveedor
from .models import CategoriaProducto,ProductoInterno
from .forms import ProductoInternoForm
import csv

# Create your views here.


#Importacion de datos de categoria.csv
def importarCategoria(request):
    with open("C:/Users/Juan Jose/Documents/DjangoProyectoI/categorias.csv",mode="r")as f:
        datos=csv.reader(f)
        next(datos)
        for row in datos:
            id,categoria=row
            cate=CategoriaProducto.objects.create(
                id=id,
                categoria=categoria
            )

    return HttpResponse("Datos exportados exitosamente")



#importacion de datos producto.csv
def importarProducto(request):
    ruta="C:/Users/Juan Jose/Documents/DjangoProyectoI/Producto.csv"
    with open(ruta,mode="r")as f:
        datos=csv.reader(f)
        next(datos)
        for row in datos:
            id,producto,ingredientes,proveedor,cat_producto,precio_p,precio_m,precio_g,existencia,date_add,foto=row
            id_proveedor=Proveedor.objects.get(pk=proveedor)
            id_catProd=CategoriaProducto.objects.get(pk=cat_producto)
            p=ProductoInterno.objects.create(
                id=id,
                producto=producto,
                ingredientes=ingredientes,
                proveedor=id_proveedor,
                cat_producto=id_catProd,
                precio_p=precio_p,
                precio_m=precio_m,
                precio_g=precio_g,
                existencia=existencia,
                date_add=date_add,
                foto=foto
            )
    return HttpResponse("Datos producto Interno exportado exitosamente")        
#########################################################

#PRODUCTO INTERNO 

class ProductoInternoCreateView(CreateView):
    model = ProductoInterno
    form_class=ProductoInternoForm
    template_name = "productos/productoInterno.html"
    success_url=reverse_lazy('producto:listaProductoInterno')


class ProductoInternoListView(ListView):
    model= ProductoInterno
    template_name = "productos/listaProductoInterno.html"
    context_object_name='prodInterno'
    











