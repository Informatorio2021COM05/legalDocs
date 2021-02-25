from django.db.models.expressions import F
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from cuentas.models import CustomUser, Escribano
from .models import Documento
from .forms import TurnoForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class HomePageView(TemplateView):
    template_name = 'principal/index.html'



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



def perfil_usuario(request):
    return render(request, 'principal/perfil_usuario.html', context=None)

class PerfilUsuario(TemplateView):
    template_name = 'principal/perfil_usuario.html'



class EditarUsuarioView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'principal/editar_cliente.html'
    fields = '__all__'
    login_url = '/cuentas/login/'



class DetalleEscribanoView(DetailView):
    model = Escribano
    template_name = 'principal/detalle_escribano.html'

    def get_context_data(self, **kwargs):
        context = super(DetalleEscribanoView, self).get_context_data(**kwargs)
        context.update({
            'usuarios_list': CustomUser.objects.all,
            'usuario_logueado': self.request.user,
            })
        return context



class ConfirmarTurnoView(LoginRequiredMixin, CreateView):
    form_class = TurnoForm
    success_url = reverse_lazy('principal:mensaje_confirmacion')
    template_name = 'principal/confirmar_turno.html'
    login_url = '/cuentas/login/'

    def get_context_data(self, **kwargs):
        context = super(ConfirmarTurnoView, self).get_context_data(**kwargs)
        context.update({
            'usuarios_list': CustomUser.objects.all,
            })
        return context

    def form_valid(self, form):
        form.instance.cliente = self.request.user
        pk = self.kwargs['pk']
        form.instance.escribano = CustomUser.objects.get(id = pk)
        return super().form_valid(form)



class MensajeConfirmacionView(TemplateView):
    template_name = 'principal/mensaje_confirmacion.html'



class CargarDocumentoView(LoginRequiredMixin, CreateView):
    model = Documento
    template_name = 'principal/cargar_documento.html'
    fields = ['titulo', 'descripcion', 'paginas', 'cliente']
    login_url = '/cuentas/login/'

    def form_valid(self, form):
        form.instance.escribano = self.request.user
        return super().form_valid(form)



class DetalleDocumentoView(LoginRequiredMixin, DetailView):
    model = Documento
    template_name = 'principal/detalle_documento.html'
    slug_field = 'slug'
    login_url = '/cuentas/login/'



class EditarDocumentoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= Documento
    fields= ('titulo', 'descripcion', 'paginas', 'archivo')
    template_name = 'principal/editar_documento.html'
    slug_field = 'slug'
    login_url = '/cuentas/login/'

    def test_func(self):
        obj = self.get_object()
        return obj.escribano == self.request.user or obj.cliente == self.request.user



def validar(request):
    if request.method == 'POST':
        codigo = request.POST['validar']
        return redirect('principal:detalle_documento', slug= codigo)
    return render(request, 'principal/validar.html')