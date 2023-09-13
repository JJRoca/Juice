from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission

class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name
    
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_password_token = models.CharField(max_length=100, blank=True, null=True)
    reset_password_requested_at = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'Pelfil de{self.user.username}'


#MODELO TIPO
class Tipo(models.Model):
    tipo=models.CharField(max_length=100)
    usuario_id=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    status=models.SmallIntegerField(default=1)

    def __str__(self):
        return str(self.id)+"-"+self.tipo