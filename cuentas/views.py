from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


class SignUpSuccesfulView(TemplateView):
    template_name = 'registration/signup_successful.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('registro_exitoso')
    template_name = 'registration/signup.html'