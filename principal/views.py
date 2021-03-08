from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from cuentas.models import CustomUser, Escribano
from .models import Documento, Turno
from .forms import DocumentoForm, TurnoForm, EditarTurnoForm, EditarDocumentoForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime


class HomePageView(TemplateView):
    template_name = 'principal/index.html'



class BuscadorView(ListView):
    model = Escribano
    template_name = 'principal/buscador_escribano.html'
    context_object_name = 'escribanos_list'

    def get_context_data(self, **kwargs):
        context = super(BuscadorView, self).get_context_data(**kwargs)
        context.update({
            'usuarios_list': CustomUser.objects.all().filter(is_escribano = True)
            })
        return context

    def get_queryset(self):
        queryset = self.request.GET.get("buscar","")
        context = Escribano.objects.filter(
            Q(ciudad__icontains = queryset) |
            Q(provincia__icontains = queryset)
        ).distinct()
        return context



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



class ConfirmarTurnoView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = TurnoForm
    success_url = reverse_lazy('principal:mensaje_confirmacion')
    template_name = 'principal/confirmar_turno.html'
    login_url = '/cuentas/login/'

    def get_context_data(self, **kwargs):
        context = super(ConfirmarTurnoView, self).get_context_data(**kwargs)
        context.update({
            'usuarios_list': CustomUser.objects.all,
            'escribano_id': self.kwargs['pk'],
            })
        return context

    def form_valid(self, form):
        form.instance.cliente = self.request.user
        pk = self.kwargs['pk']
        form.instance.escribano = CustomUser.objects.get(id = pk)
        return super().form_valid(form)
    
    def test_func(self):
        if not self.request.user.is_escribano:
            return self.request.user



class MensajeConfirmacionView(TemplateView):
    template_name = 'principal/mensaje_confirmacion.html'



class CargarDocumentoView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = DocumentoForm
    template_name = 'principal/cargar_documento.html'
    login_url = '/cuentas/login/'

    def form_valid(self, form):
        form.instance.escribano = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_escribano



class DetalleDocumentoView(LoginRequiredMixin, DetailView):
    model = Documento
    template_name = 'principal/detalle_documento.html'
    slug_field = 'slug'
    login_url = '/cuentas/login/'

    def get_context_data(self, **kwargs):
        context = super(DetalleDocumentoView, self).get_context_data(**kwargs)
        context.update({
            'usuario_logueado': self.request.user,
            })
        return context



class EditarDocumentoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= Documento
    form_class = EditarDocumentoForm
    template_name = 'principal/editar_documento.html'
    slug_field = 'slug'
    login_url = '/cuentas/login/'

    def test_func(self):
        obj = self.get_object()
        return obj.escribano == self.request.user



def validar(request):
    if request.method == 'POST':
        codigo = request.POST['validar']
        return redirect('principal:detalle_documento', slug= codigo)
    return render(request, 'principal/validar.html')



class ListaDocumentos(LoginRequiredMixin, ListView):
    model = Documento
    template_name = 'principal/lista_documentos.html'
    context_object_name = 'documentos_list'
    login_url = '/cuentas/login/'

    def get_queryset(self):
        if self.request.user.is_escribano:
            return super(ListaDocumentos, self).get_queryset().filter(escribano=self.request.user)
        else:
            return super(ListaDocumentos, self).get_queryset().filter(cliente=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ListaDocumentos, self).get_context_data(**kwargs)
        context.update({
            'usuario': self.request.user,
            })
        return context



class ListaTurnos(LoginRequiredMixin, ListView):
    model = Turno
    template_name = 'principal/lista_turnos.html'
    context_object_name = 'turnos_list'
    login_url = '/cuentas/login/'

    def get_queryset(self):
        if self.request.user.is_escribano:
            return super(ListaTurnos, self).get_queryset().filter(escribano=self.request.user).order_by('fecha', 'hora', '-creacion')
        else:
            return super(ListaTurnos, self).get_queryset().filter(cliente=self.request.user).order_by('fecha', 'hora', '-creacion')

    def get_context_data(self, **kwargs):
        context = super(ListaTurnos, self).get_context_data(**kwargs)
        now = datetime.date(datetime.now())
        context.update({
            'usuario': self.request.user,
            'now': now,
            })
        return context



class EditarTurno(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Turno
    form_class = EditarTurnoForm
    template_name = 'principal/editar_turno.html'
    success_url = '/turnos/'
    login_url = '/cuentas/login/'

    def test_func(self):
        obj = self.get_object()
        return obj.escribano == self.request.user