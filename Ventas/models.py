from django.db import models
from cliente.models import Cliente
from Producto.models import CategoriaProducto,ProductoInterno
# Create your models here.
# class Factura(models.Model):
#     fecha=models.DateTimeField(auto_now=False,auto_now_add=False)
#     # usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
#     codCliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
#     totalFactura=models.DecimalField(max_digits=6,decimal_places=2)
#     status=models.PositiveSmallIntegerField(default=1)

#     def __str__(self):
#         return str(self.id)+"-"+self.usuario.nombre

class Pedido(models.Model):
    fecha_pedido = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido {self.id}"


class DetalleFactura(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,blank=True,null=True)
    codProductoIn=models.ForeignKey(ProductoInterno,on_delete=models.CASCADE)
    ingrediente=models.CharField(max_length=50,null=True,blank=True)
    extras=models.CharField(max_length=100,null=True,blank=True)
    cantidad=models.PositiveIntegerField(null=True,blank=True)
    precio_venta=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    total_venta=models.DecimalField(max_digits=7,decimal_places=2)
    fecha_venta=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)+"-"+self.codProductoIn.producto
    
class Detalle_temp(models.Model):
    toke_user=models.CharField(max_length=50)
    categoria_producto=models.ForeignKey(CategoriaProducto,on_delete=models.CASCADE)
    codProductoIn=models.ForeignKey(ProductoInterno,on_delete=models.CASCADE)
    ingredientes=models.CharField(max_length=50,default='Sin ingredientes')
    extras=models.CharField(max_length=50,default='S/E')
    tamaño=models.CharField(max_length=10)
    cantidad=models.PositiveIntegerField()
    precio_venta=models.DecimalField(max_digits=5,decimal_places=2)
    paraLlevar=models.CharField(max_length=50,default='No')

    def __str__(self):
        return str(self.id)+"-"+self.toke_user


# class Pedidos(models.Model):
#     noFactura=models.ForeignKey(Factura,on_delete=models.CASCADE)    
#     categoria_producto=models.ForeignKey(CategoriaProducto,on_delete=models.CASCADE)
#     codProductoIn=models.ForeignKey(ProductoInterno,on_delete=models.CASCADE)
#     ingrediente=models.CharField(max_length=50,null=True,blank=True)
#     extras=models.CharField(max_length=100,null=True,blank=True)
#     cantidad=models.PositiveIntegerField(null=True,blank=True)
#     paraLlevar=models.CharField(max_length=50,null=True,blank=True)
#     fecha=models.DateTimeField(auto_now=False,auto_now_add=False)
#     idusuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
#     idcliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
#     status=models.IntegerField(default=1)
#     def __str__(self):
#         return str(self.id)+"-"+self.codProductoIn.descripcion

