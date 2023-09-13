 #cliente form       
from .models import Cliente
from django import forms

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['nit','nombre','telefono','direccion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ci'].widget.attrs.update({'placeholder':'Numero de C.I.','id':'ci','name':'ci'})
        self.fields['nombre'].widget.attrs.update({'name':"nombre",'id':'nombre','placeholder':'Ingrese Nombre'})
        self.fields['telefono'].widget.attrs.update({'name':'telefono','id':'telefono','placeholder':'Ingrese Telefono'})
        self.fields['direccion'].widget.attrs.update({'name':'direccion','id':'direccion','placeholder':'Ingrese Direccion'})


