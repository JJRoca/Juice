from django.urls import path
from . import views
app_name='producto'
urlpatterns = [
    #Importacion de datos
    # path('importacion/',views.importarCategoria),
    # #Imporatcion de datos producto
    # path('importarProducto/',views.importarProducto),
    path('listaProductoInterno/',views.ProductoInternoListView.as_view(),name='listaProductoInterno'),
    path('registrarProductoInterno/',views.ProductoInternoCreateView.as_view(),name='registrarProductoInterno')
]