from django.http.response import HttpResponse, HttpResponseBase
from django.shortcuts import render
from cuentas.models import CustomUser, Escribano
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.db.models import Q
from django.forms.models import model_to_dict
from django.db.models import Model


class HomePageView(TemplateView):
    template_name = 'principal/index.html'



def validar_documento(request):
    return render(request, 'principal/validar_documento.html', context=None)

def cargar_documento(request):
    return render(request, 'principal/cargar_documento.html', context=None)

def buscador_escribano(request):
    queryset = request.GET.get("buscar")
    escribano = Escribano.objects.all()
    if queryset:
        escribano = Escribano.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(apellido__icontains = queryset)
        ).distinct()
    return render(request, 'principal/buscador_escribano.html', {'escribano':escribano})



class BuscadorView(ListView):
    model = Escribano
    template_name = 'principal/buscador_escribano.html'
    context_object_name = 'escribanos_list'

    def get_context_data(self, **kwargs):
        context = super(BuscadorView, self).get_context_data(**kwargs)
        context.update({
            'usuarios_list': CustomUser.objects.all
            })
        return context

    def get_queryset(self):
        return Escribano.objects.all



def perfil_cliente(request):
    return render(request, 'principal/perfil_cliente.html', context=None)

class EditarUsuarioView(UpdateView):
    model = CustomUser
    template_name = 'principal/editar_cliente.html'
    fields = '__all__'

class DetalleEscribanoView(DetailView):
    model = Escribano
    template_name = 'principal/detalle_escribano.html'

#    def get_context_data(self, **kwargs):
#        context = super(BuscadorView, self).get_context_data(**kwargs)
#        context.update({
#            'usuarios_list': CustomUser.objects.all
#            })
#        return context
#
#    def get_queryset(self):
#        return Escribano.objects.all

def perfil_escribano_publico(request):
    return render(request, 'principal/perfil_escribano_desde_usuario.html', context=None)

def perfil_escribano(request):
    return render(request, 'principal/perfil_escribano.html', context=None)

def resultado_busqueda(request):
    return render(request, 'principal/resultado_busqueda.html', context=None)