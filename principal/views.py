from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render


def log_in(request):
    #template = loader.get_template('principal/login.html')
    return render(request, 'principal/login.html', context=None)

def sign_up(request):
    #template = loader.get_template('principal/signup.html')
    return render(request, 'principal/signup.html', context=None)