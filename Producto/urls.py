from django.urls import path
from . import views
app_name='producto'
urlpatterns = [
    path('listaProductoInterno/',views.ProductoInternoListView.as_view(),name='listaProductoInterno'),
    path('registrarProductoInterno/',views.ProductoInternoCreateView.as_view(),name='registrarProductoInterno')
]