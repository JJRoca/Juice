from django.urls import path
from . import views
urlpatterns = [
    # path('importacionFactura/',views.importar),
    path('listar-categorias/', views.listar_categorias, name='listar_categorias'),
    path('consulta-productos/', views.consulta_productos, name='consulta_productos'),    

    path('guardar_detalles/', views.guardar_detalles, name='guardar_detalles'),
    path('despachar/<int:detalle_id>/',views.despachar_producto,name='despachar_producto'),
    path('detalle_factura/',views.detalle_factura,name='detalle_factura')
]