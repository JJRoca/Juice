from django.http import JsonResponse
from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm
from django.views.generic import TemplateView,CreateView,ListView,View,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

class ClienteCreateView(CreateView):
    model=Cliente
    form_class=ClienteForm
    template_name = "clientes/registroCliente.html"
    success_url=reverse_lazy('persona:listaCliente')
class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/listaCliente.html"
    context_object_name='clien'

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/editarCliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente actualizado con éxito.')
        return reverse_lazy('persona:editarCliente', kwargs={'pk': self.object.pk})
    
def buscar_cliente(request):
    nit = request.GET.get('nit')
    print("nit------------")
    print(nit)
    cliente = Cliente.objects.filter(nit=nit).first()
    data = {'cliente': None}
    if cliente:
        data['cliente'] = {
            'id': cliente.id,
            'nit': cliente.nit,
            'nombre': cliente.nombre,
            'direccion': cliente.direccion,
            'telefono': cliente.telefono
            # agregar mas campos si es q se necesita
        }
    else:
        print("Cliente no encontrado")    
    print("datos-----------------------------------------")
    print(data['cliente'])
    return JsonResponse(data)