from django.db import models
from cliente.models import Proveedor
# Create your models here.
class CategoriaProducto(models.Model):
    categoria=models.CharField(max_length=100)
    status=models.SmallIntegerField(default=1)
    def __str__(self):
        return str(self.id)+"-"+self.categoria+"-"
    
class ProductoInterno(models.Model):
    producto=models.CharField(max_length=100,blank=True,null=True)
    ingredientes=models.CharField(max_length=400)    
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE,blank=True,null=True)
    cat_producto=models.ForeignKey(CategoriaProducto,on_delete=models.CASCADE)
    precio_p=models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    precio_m=models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    precio_g=models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    existencia=models.SmallIntegerField(blank=True,null=True)
    date_add=models.DateTimeField()
    foto=models.ImageField(upload_to="media/")
    def __str__(self):
        return self.producto

