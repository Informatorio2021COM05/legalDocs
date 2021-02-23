from .forms import CustomUserCreationForm, EscribanoCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect


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