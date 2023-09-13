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

# Create your views here.

#lista toda las categorias que hay en el modelo Categoria
def listar_categorias(request):
    #Hacemos uso del ORM de django para traer todos los datos que hay en el modelo Categoria
    categorias = CategoriaProducto.objects.all().order_by('categoria')                           
    # Renderizamos la plantilla 'categorias.html' y pasamos el conjunto de datos 'categorias' al contexto de la plantilla
    return render(request, 'categorias.html', {'categorias': categorias})
  
 

def consulta_productos(request):
    # Verificamos si la solicitud es una petición AJAX GET
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Obtenemos el identificador de la categoría desde los parámetros GET
        categoria_id = request.GET.get('categoriaId')
        # Realizamos una consulta a la base de datos usando el ORM de django para obtener productos internos
        # que pertenecen a la categoría especificada
        productos_internos = ProductoInterno.objects.filter(cat_producto_id=categoria_id)
        
        # Inicializamos una lista vacía para almacenar los datos de los productos
        productos_data = []

        for producto_interno in productos_internos:
            # Dividimos la cadena de ingredientes y creamos una lista de opciones
            ingredientes = producto_interno.ingredientes.split('/')
            selectOptions = ''
            
            # Generamos opciones HTML para cada ingrediente
            for ingrediente in ingredientes:
                selectOptions += '<option value="' + ingrediente.strip() + '">' + ingrediente.strip() + '</option>'
            
            # Creamos un diccionario con datos del producto
            producto_data = {
                'producto': producto_interno.producto,
                'ingredientes': ingredientes,  # Ahora se guarda la lista de ingredientes
                'proveedor': producto_interno.proveedor.proveedor,
                'precio_p': str(producto_interno.precio_p),
                'precio_m': str(producto_interno.precio_m),
                'precio_g': str(producto_interno.precio_g),
                'selectOptions': selectOptions  # Agrega las opciones al diccionario    
            }
            # Agregamos los datos del producto a la lista
            productos_data.append(producto_data)

            # Imprimimos los datos del producto en la consola (esto es útil para fines de depuración)
            print(producto_data)

        # Devolvemos una respuesta JSON con los datos de los productos
        return JsonResponse({'productosInternos': productos_data})
    # Si no es una solicitud AJAX o no es una solicitud GET, puedes devolver un error o redirigir a otra página
    return JsonResponse({'error': 'Invalid request'})

def guardar_detalles(request):
    # Verificamos si la solicitud es un POST
    if request.method == 'POST':
        # Cargamos los datos JSON enviados en el cuerpo de la solicitud
        data = json.loads(request.body)
        
        # Obtenemos los detalles y el número de identificación del cliente (NIT) del objeto 'data'
        detalles = data.get('detalles', [])
        nit_cliente = data.get('nit_cliente')
        
         # Imprimimos información de depuración para verificar los datos recibidos
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
            
            # Creamos un nuevo registro de cliente en la base de datos
            cliente = Cliente(
                nit=nit_cliente,
                nombre=nombre_cliente,
                telefono=telefono_cliente
            )
            cliente.save()

        pedido = Pedido.objects.create()  # Se creará un nuevo pedido automáticamente
        # Iteramos a través de los detalles de la factura y los guardamos en la base de datos
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

        # Devolvemos una respuesta JSON indicando que los detalles de la factura se han guardado exitosamente
        return JsonResponse({'message': 'Detalles de factura guardados exitosamente.'})
    else:
        # Si la solicitud no es un POST, devolvemos un error
        return JsonResponse({'error': 'Método no permitido.'})

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
    #creamos un diccionario
    detalles_por_pedido = {}

    for detalle in detalles:
        pedido_id = detalle.pedido_id
        if pedido_id not in detalles_por_pedido:
            detalles_por_pedido[pedido_id] = []
        detalles_por_pedido[pedido_id].append(detalle)
        
    context = {'detalles_por_pedido': detalles_por_pedido}
    return render(request, 'detalle_factura.html', context)