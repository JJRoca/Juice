from django.contrib import admin
from .models import CategoriaProducto,ProductoInterno

class ProductoInternoAdmin(admin.ModelAdmin):
    list_display=['id','producto','ingredientes','proveedor','precio_p','precio_m','precio_g']
    search_fields=['producto']
 
admin.site.register(CategoriaProducto)
admin.site.register(ProductoInterno,ProductoInternoAdmin)
