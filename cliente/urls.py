from django.urls import path
from . import views

app_name='persona'
urlpatterns = [
    path('login/',views.iniciar_sesion,name='login'),
    
    #pdf
    path('pdf/',views.DescargarPDF.as_view(),name='pdf'),
    path('importar/',views.importar),
    path('',views.InicioTemplante.as_view(),
         name='inicio'),
    path('añadirRol/',views.RolCreateView.as_view(),name='añadirRol'),
    path('listaRol/',views.RolListView.as_view(),name='listaRol'),
############################################################
    path('registrarUsuario/',
         views.UsuarioCreateView.as_view(),
         name='registrarUsuario'),
    path('listarUsuarios/',
         views.UsuarioListView.as_view(),
         name='listaUsuario'),
    path('editarUsuario/<int:pk>',views.UsuarioUpdateView.as_view(),name='editarUsuario'),
############################################
          
          #CLIENTE
    path('pdfCliente/',views.DescargarPDFCliente.as_view(),name='pdfCliente'),
    path('registrarCliente/',
         views.ClienteCreateView.as_view(),
         name='registrarCliente'),
    path('listaCliente/',
         views.ClienteListView.as_view(),
         name='listaCliente'),
    path('editarCliente/<int:pk>',
          views.ClienteUpdateView.as_view(),
          name='editarCliente'),

    path('registrarProveedor/',
         views.ProveedorCreateView.as_view(),
         name='registrarProveedor'),     
    path('listaProveedor/',
         views.ProveedorListView.as_view(),name='listaProveedor'),
     
     path('editarProveedor<int:pk>/',views.ProveedorUpdateView.as_view(),name='editarProveedor'),

     #BUSCAR CLIENTE POR NIT
     path('buscar_cliente/',views.buscar_cliente,name='buscar_cliente'),
     path('guardar_detalles/', views.guardar_detalles, name='guardar_detalles'),
     path('plantilla-pedido/', views.plantilla_pedido, name='plantilla_pedido'),
     path('actualizar_estado/',views.actualizar_estado,name='actualizar_estado'),
     path('despachar_productos/',views.despachar_productos,name='despachar_productos')
]
