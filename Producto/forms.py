from django.core.validators import MinValueValidator
from .models import Proveedor,ProductoInterno,CategoriaProducto
from django import forms

#FORMULARIO QUE SE CREA A PARTIR DEL MODELO PRODUCTOEXTERNO

#FORMULARIO PARA PRODUCTO INTERNO

class ProductoInternoForm(forms.ModelForm):
    
    class Meta:
        model=ProductoInterno
        #CAMPOS QUE TIENE EL MODELO PRODUCTO EXTERNO ESPECIFICAR CUALES SE ENVIARAN A LA PLANTILLA
        fields=['proveedor','cat_producto','producto','precio_p','precio_m','precio_g','ingredientes']
        # exclude=['usuario_id','existencia']

        widgets={
            'proveedor':forms.Select(),
            'cat_producto':forms.Select(),
            'producto':forms.TextInput(attrs={'placeholder':'Ingrese nombre del producto'}),
            'precio_p': forms.NumberInput(attrs={'step': '00.00','placeholder':'0.00'}),
            'precio_m': forms.NumberInput(attrs={'step': '00.00','placeholder':'0.00'}),
            'precio_g': forms.NumberInput(attrs={'step': '00.00','placeholder':'0.00'}),
            'ingredientes':forms.TextInput(attrs={'placeholder':'Ingrese ingredientes del producto'}),
        }
                
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario_id'].initial=1
        self.fields['proveedor'].widget.choices = [('','Seleccione Proveedor')] + [(prov.id, prov.proveedor) for prov in Proveedor.objects.all()]
        self.fields['cat_producto'].widget.choices=[('','Seleccione Categoria')]+[(cat.id,cat.categoria) for cat in CategoriaProducto.objects.all()]
