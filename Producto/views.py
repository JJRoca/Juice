from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from django.http import HttpResponse
from cliente.models import Proveedor
from .models import CategoriaProducto,ProductoInterno
from .forms import ProductoInternoForm
import csv

# Create your views here.


#PRODUCTO EXTERNO 



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
    











