from django.db import models

#MODELOS CLIENTE
class Cliente(models.Model):
    nit=models.CharField(max_length=20,blank=True,null=True,unique=True)
    nombre=models.CharField(max_length=80,blank=True,null=True)
    telefono=models.PositiveIntegerField(blank=True,null=True)
    direccion=models.TextField(blank=True,null=True)
    dateadd=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)+"-"+(self.nombre or "")
    
class Proveedor(models.Model):
    proveedor=models.CharField(max_length=100)
    contacto=models.CharField(max_length=100,blank=True,null=True)
    telefono=models.PositiveIntegerField(blank=True,null=True)
    direccion=models.TextField(blank=True,null=True)
    date_add=models.DateTimeField(auto_now_add=True)
    status=models.SmallIntegerField(default=1)
    def __str__(self):
        return str(self.id)+"-"+self.proveedor