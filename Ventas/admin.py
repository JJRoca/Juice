from django.contrib import admin
from .models import DetalleFactura,Detalle_temp,Pedido
# Register your models here.
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display=['id','cliente','status','codProductoIn','ingrediente','precio_venta','cantidad','pedido','total_venta','fecha_venta']

admin.site.register(DetalleFactura,DetalleFacturaAdmin)
admin.site.register(Detalle_temp)
admin.site.register(Pedido)