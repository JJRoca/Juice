from django.http import JsonResponse
from django.template.loader import render_to_string
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse
import csv
from django.views.generic import CreateView
from cliente.models import  Cliente
from Producto.models import CategoriaProducto,ProductoInterno
from .models import DetalleFactura,Pedido
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
# def importar(request):
  
#     with open('C://Users//Juan Jose//Documents//ImportacionDatos//pedidos.csv','r')as f:
#         datos=csv.reader(f)
#         next(datos)
#         for row in datos:
#             idpedido,nofactura,categoria_producto,codproducto_in,ingrediente,extras,cantidad,paraLlevar,fecha,idusuario,idcliente,status=row
#             id_factura=Factura.objects.get(pk=nofactura)
#             id_categoria_producto=CategoriaProducto.objects.get(pk=categoria_producto)
#             id_codProducto =ProductoInterno.objects.get(pk=codproducto_in)
#             usuario_id=Usuario.objects.get(pk=idusuario)
#             cliente_id=Cliente.objects.get(pk=idcliente)

#             pedi=Pedido.objects.create(
#                 id=idpedido,
#                 noFactura=id_factura,
#                 categoria_producto=id_categoria_producto,
#                 codProductoIn=id_codProducto,
#                 ingrediente=ingrediente,
#                 extras=extras,
#                 cantidad=cantidad,
#                 paraLlevar=paraLlevar,
#                 fecha=fecha,
#                 idusuario=usuario_id,
#                 idcliente=cliente_id,
#                 status=status
#             )
#             pedi.save()

        
#     return HttpResponse("Se guardo exitosamente")

#GUARDAR VENTAS
def guardar_detalles(request):
    #verificamos si un post 
    if request.method == 'POST':
        data = json.loads(request.body)
        detalles = data.get('detalles', [])
        nit_cliente = data.get('nit_cliente')
        print(f"Dataaaaaa: {data}, tipo {type(data)}")
        print("detalles")
        print(detalles)
        print("tipo de objeto",type(detalles))
        print("nit cliente---------")
        print(nit_cliente)
        #Verificar si el cliente ya existe en la base de dat<os
        try:
            cliente = Cliente.objects.get(nit=nit_cliente)
        except Cliente.DoesNotExist:
            # El cliente no existe, registrar al cliente primero
            cliente_data = detalles.pop()  # Extraer los datos del cliente del objeto detalles
            nombre_cliente = cliente_data.get('nombre_cliente')
            telefono_cliente = cliente_data.get('telefono_cliente')
            print("-----------------------------------------------------------------------")
            print(cliente_data)
            cliente = Cliente(
                nit=nit_cliente,
                nombre=nombre_cliente,
                telefono=telefono_cliente
            )
            cliente.save()
        pedido = Pedido.objects.create()  # Se creará un nuevo pedido automáticamente
        for detalle in detalles:
            producto = detalle.get('producto')
            if producto:
                ingrediente = detalle.get('ingrediente')
                cantidad = detalle.get('cantidad')
                precio_venta = detalle.get('precio_venta')
                extras = detalle.get('extras')
                total_venta = detalle.get('total_venta')
                print(f"producto: {producto}, ingrediente: {ingrediente}, cantidad: {cantidad}")
                detalle_factura = DetalleFactura(
                    pedido=pedido,
                    cliente=cliente,
                    codProductoIn=ProductoInterno.objects.get(producto=producto),
                    ingrediente=ingrediente,
                    extras=extras,
                    cantidad=cantidad,
                    precio_venta=precio_venta,          
                    total_venta=total_venta
                )
                detalle_factura.save()
                print("detallessssss: ",detalle_factura)
            else:
                print("Error")
        return JsonResponse({'message': 'Detalles de factura guardados exitosamente.'})
    else:
        return JsonResponse({'error': 'Método no permitido.'})

def productos_por_categoria(request, categoria_id):
    productos = ProductoInterno.objects.filter(cat_producto_id=categoria_id)
    categorias = CategoriaProducto.objects.all()
    context = {'productos': productos, 'categorias': categorias}
    return render(request, 'nuevaVenta.html', context)


def index(request):
    categorias = CategoriaProducto.objects.all()
    return render(request, 'inicio.html', {'categorias': categorias})
def productos(request, cat_id=None):
    categorias = CategoriaProducto.objects.all()
    productos = ProductoInterno.objects.filter(cat_producto=cat_id) if cat_id else None
    context = {'categorias': categorias, 'productos': productos}

    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Si la solicitud es una solicitud AJAX, devolver una respuesta JSON
        data = {'html': render_to_string('productos.html', context)}
        return JsonResponse(data)
    else:
        # Si la solicitud no es una solicitud AJAX, renderizar la plantilla
        return render(request, 'productos.html', context)




def listar_categorias(request):
    categorias = CategoriaProducto.objects.all().order_by('categoria')
    return render(request, 'categorias.html', {'categorias': categorias})
 
def listar_productos(request, categoria_id):
    productos = ProductoInterno.objects.filter(cat_producto_id=categoria_id)
    data = {'productos': []}
    for producto in productos:
        ingredientes = producto.ingredientes.split("/")
        data['productos'].append({
            'producto': producto.producto,
            'ingredientes':ingredientes,
            'precio_p': producto.precio_p,
            'precio_m': producto.precio_m,
            'precio_g': producto.precio_g,
        })
    print("********************************************"+ingredientes)    
    return JsonResponse(data)   
  
#GUARDAR DATOS EN EL MODELO DETALLEFACTURA
def guardar_detalles_factura(request):
    if request.method == 'POST' and 'HTTP_X_REQUESTED_WITH' in request.headers and request.headers['HTTP_X_REQUESTED_WITH'] == 'XMLHttpRequest':
        body_unicode = request.body.decode('utf-8')
        detalles = json.loads(body_unicode)
        
        if detalles:
            for detalle in detalles:
                # Obtener la descripción del producto interno
                producto_desc = detalle['producto']
                producto_interno = ProductoInterno.objects.get(descripcion=producto_desc)
                
                # Crear un nuevo objeto DetalleFactura y asignar los valores correspondientes
                detalle_factura = DetalleFactura()
                detalle_factura.producto = producto_interno
                detalle_factura.cantidad = detalle['cantidad']
                detalle_factura.precio = detalle['precio']
                detalle_factura.total = detalle['total']
                detalle_factura.extras = detalle['extras']
                detalle_factura.save()
            
            return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})

def consulta_productos(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        categoria_id = request.GET.get('categoriaId')
        productos_internos = ProductoInterno.objects.filter(cat_producto_id=categoria_id)
        productos_data = []

        for producto_interno in productos_internos:
            # Divide los ingredientes y crea una lista de opciones
            ingredientes = producto_interno.ingredientes.split('/')
            selectOptions = ''

            for ingrediente in ingredientes:
                selectOptions += '<option value="' + ingrediente.strip() + '">' + ingrediente.strip() + '</option>'

            producto_data = {
                'producto': producto_interno.producto,
                'ingredientes': ingredientes,  # Ahora se guarda la lista de ingredientes
                'proveedor': producto_interno.proveedor.proveedor,
                'precio_p': str(producto_interno.precio_p),
                'precio_m': str(producto_interno.precio_m),
                'precio_g': str(producto_interno.precio_g),
                'selectOptions': selectOptions  # Agrega las opciones al diccionario    
            }
            productos_data.append(producto_data)

            print(producto_data)

        return JsonResponse({'productosInternos': productos_data})
    # Si no es una solicitud AJAX o no es una solicitud GET, puedes devolver un error o redirigir a otra página
    return JsonResponse({'error': 'Invalid request'})

#Para el boton despachar de la plantilla detalle_factura cada vez q hagamos click en despachar se cambiara de false a true
def despachar_producto(request, detalle_id):
    detalle = DetalleFactura.objects.get(id=detalle_id)
    detalle.status = True
    detalle.save()
    # return JsonResponse({'message': 'success'})
    response = JsonResponse({'message': 'success'})

    # Agregar encabezados para evitar caché
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response
#detalle factura para agrupar por pedido
def detalle_factura(request):
    #traemos todos los datos de detalleFactura cuyo status sea false y lo ordemos por numero de pedido
    detalles = DetalleFactura.objects.filter(status=False).order_by('pedido__id')
    print(detalles)
    detalles_por_pedido = {}

    for detalle in detalles:
        pedido_id = detalle.pedido_id
        if pedido_id not in detalles_por_pedido:
            detalles_por_pedido[pedido_id] = []
        detalles_por_pedido[pedido_id].append(detalle)
        
    context = {'detalles_por_pedido': detalles_por_pedido}
    return render(request, 'detalle_factura.html', context)