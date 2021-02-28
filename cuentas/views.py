from django.urls.base import set_urlconf
from .forms import CustomUserCreationForm, EscribanoCreationForm
from .models import CustomUser
from django.urls import reverse_lazy
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



class PerfilUsuario(TemplateView):
    template_name = 'principal/perfil_usuario.html'

class EditarUsuarioView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'principal/editar_perfil.html'
    fields = '__all__'
    login_url = '/cuentas/login/'
    # success_url = reverse_lazy('/cuentas/login/')

    # No muestra el id
    # def get_object(self, queryset:None):
    #     return self.request.user
