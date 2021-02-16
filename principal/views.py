from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render


def log_in(request):
    #template = loader.get_template('principal/login.html')
    return render(request, 'principal/login.html', context=None)

def sign_up(request):
    #template = loader.get_template('principal/signup.html')
    return render(request, 'principal/signup.html', context=None)

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