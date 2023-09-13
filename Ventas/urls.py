from django.urls import path
from . import views
urlpatterns = [
    # path('importacionFactura/',views.importar),
    path('productos/categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('inicio123/', views.index, name='venta'),

    path('productos/', views.productos, name='productos'),
    path('productos/<int:cat_id>/', views.productos, name='productos_por_categoria'),
     

  
    path('listar-categorias/', views.listar_categorias, name='listar_categorias'),
    path('consulta-productos/', views.consulta_productos, name='consulta_productos'),
    path('guardar-detalles-factura/', views.guardar_detalles_factura, name='detalleFactura'),
    
    
    path('listar-productos/<int:categoria_id>/', views.listar_productos, name='listar_productos'),
    path('guardar_detalles/', views.guardar_detalles, name='guardar_detalles'),
    path('despachar/<int:detalle_id>/',views.despachar_producto,name='despachar_producto'),
    path('detalle_factura/',views.detalle_factura,name='detalle_factura')
]