from django.urls.base import set_urlconf
from .forms import CustomUserCreationForm, EscribanoCreationForm
from .models import CustomUser
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('registro_exitoso')
    template_name = 'registration/signup.html'



class EscribanoSignUpView(CreateView):
    form_class = EscribanoCreationForm
    success_url = reverse_lazy('registro_exitoso')
    template_name = 'registration/signup_escribano.html'



class SignUpSuccesfulView(TemplateView):
    template_name = 'registration/signup_successful.html'



class PerfilUsuario(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CustomUser
    template_name = 'registration/perfil_usuario.html'
    login_url = '/cuentas/login/'

    def test_func(self):
        obj = self.get_object()
        return obj.id == self.request.user.id


class EditarUsuarioView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    template_name = 'registration/editar_perfil.html'
    fields = ('username', 'nombre', 'apellido', 'dni')
    login_url = '/cuentas/login/'
    success_url = reverse_lazy('cuentas:perfil')


    def test_func(self):
        obj = self.get_object()
        return obj.id == self.request.user.id

    def get_success_url(self):
        return reverse('cuentas:perfil', kwargs={'pk': self.request.user.id})

    # No muestra el id
    # def get_object(self, queryset:None):
    #     return self.request.user
