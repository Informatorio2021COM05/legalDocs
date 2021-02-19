from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from principal.forms import BasicSignupForm, ExtendSignupForm, ClienteForm, EscribanoForm
import html
from principal.models import Usuario


def log_in(request):
    #template = loader.get_template('principal/login.html')
    return render(request, 'principal/login.html', context=None)

class UsuarioSignup:
    def register(request):
        if request.method == 'POST':
            usuario = request.POST['usuario']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            dni = request.POST['dni']
            email = request.POST['email']
            contraseña = request.POST['contraseña']
            confirmar_contraseña = request.POST['confirmar_contraseña']
            
            if contraseña == confirmar_contraseña:
                if Usuario.objects.filter(usuario = usuario).exists():
                    print('Usuario existente')
                elif Usuario.objects.filter(email = email).exists():
                    print('El email ya ha sido registrado')
                elif Usuario.objects.filter(dni = dni).exists():
                    print('El dni ya se encuentra registrado')
                else:
                    usuario = Usuario(usuario=usuario, nombre=nombre, apellido=apellido, dni=dni, email=email, contraseña = contraseña)
                    usuario.save()
                    return HttpResponseRedirect(reverse('index'))
        form = BasicSignupForm()
        ctx = {'form': form}
        return render(request, 'principal/signup.html', ctx)



#        form = BasicSignupForm()
#        ctx = {'form': form}
#        return render(request, 'principal/signup.html', ctx)

class ClienteSignup(UsuarioSignup):
    def get(self, request):
        form = ClienteForm

#    def sign_up(self, request):




def validar_documento(request):
    return render(request, 'principal/validar_documento.html', context=None)

def cargar_documento(request):
    return render(request, 'principal/cargar_documento.html', context=None)

def buscador_escribano(request):
    return render(request, 'principal/buscador_escribano.html', context=None)

def perfil_cliente(request):
    return render(request, 'principal/perfil_cliente.html', context=None)

def perfil_escribano_desde_usuario(request):
    return render(request, 'principal/perfil_escribano_desde_usuario.html', context=None)

def perfil_escribano(request):
    return render(request, 'principal/perfil_escribano.html', context=None)

def resultado_busqueda(request):
    return render(request, 'principal/resultado_busqueda.html', context=None)