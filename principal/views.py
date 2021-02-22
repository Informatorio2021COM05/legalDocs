from django.shortcuts import render
from cuentas.models import CustomUser, Escribano
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView


class HomePageView(TemplateView):
    template_name = 'principal/index.html'


class LoginPageView(TemplateView):
    template_name = 'registration/login.html'


#class ClienteSignup:
#    def register(request):
#        if request.method == 'POST':
#            usuario = request.POST['usuario']
#            nombre = request.POST['nombre']
#            apellido = request.POST['apellido']
#            dni = request.POST['dni']
#            email = request.POST['email']
#            contraseña = request.POST['contraseña']
#            confirmar_contraseña = request.POST['confirmar_contraseña']
#            
#            if contraseña == confirmar_contraseña:
#                if Cliente.objects.filter(usuario = usuario).exists():
#                    print('Usuario existente')
#                elif Cliente.objects.filter(email = email).exists():
#                    print('El email ya ha sido registrado')
#                elif Cliente.objects.filter(dni = dni).exists():
#                    print('El dni ya se encuentra registrado')
#                else:
#                    user = Cliente(
#                        usuario=usuario, nombre=nombre, apellido=apellido,
#                        dni=dni, email=email, contraseña = contraseña
#                    )
#                    user.save()
#                    return redirect('principal:index')
#        form = BasicSignupForm()
#        ctx = {'form': form}
#        return render(request, 'registration/signup.html', ctx)


#class EscribanoSignup:
#    def register(request):
#        if request.method == 'POST':
#            usuario = request.POST['usuario']
#            nombre = request.POST['nombre']
#            apellido = request.POST['apellido']
#            dni = request.POST['dni']
#            email = request.POST['email']
#            contraseña = request.POST['contraseña']
#            confirmar_contraseña = request.POST['confirmar_contraseña']
#            matricula = request.POST['matrícula']
#            provincia = request.POST['provincia']
#            ciudad = request.POST['ciudad']
#            calle = request.POST['calle']
#            altura = request.POST['altura']
#            piso = request.POST['piso']
#            numeroPuerta = request.POST['número_de_puerta']
#
#            if contraseña == confirmar_contraseña:
#                if Escribano.objects.filter(usuario = usuario).exists():
#                    print('Usuario existente')
#                elif Escribano.objects.filter(email = email).exists():
#                    print('El email ya ha sido registrado')
#                elif Escribano.objects.filter(dni = dni).exists():
#                    print('El dni ya se encuentra registrado')
#                else:
#                    user = Escribano(
#                        usuario=usuario, nombre=nombre, apellido=apellido,
#                        dni=dni, email=email, contraseña = contraseña,
#                        matricula=matricula, provincia=provincia,
#                        ciudad=ciudad, calle=calle, altura=altura,
#                        piso=piso, numeroPuerta=numeroPuerta
#                    )
#                    user.save()
#                    return redirect('principal:index')
#        form = ExtendSignupForm()
#        ctx = {'form': form}
#        return render(request, 'registration/signup_escribano.html', ctx)



def validar_documento(request):
    return render(request, 'principal/validar_documento.html', context=None)

def cargar_documento(request):
    return render(request, 'principal/cargar_documento.html', context=None)

def buscador_escribano(request):
    return render(request, 'principal/buscador_escribano.html', context=None)

class BuscadorView(ListView):
    model = Escribano
    template_name = 'principal/buscador_escribano.html'
    context_object_name = 'escribanos_list'

def perfil_cliente(request):
    return render(request, 'principal/perfil_cliente.html', context=None)

class EditarUsuarioView(UpdateView):
    model = CustomUser
    template_name = 'principal/editar_cliente.html'
    fields = '__all__'

class DetalleEscribanoView(DetailView):
    model = Escribano
    template_name = 'principal/detalle_escribano.html'

def perfil_escribano_publico(request):
    return render(request, 'principal/perfil_escribano_desde_usuario.html', context=None)

def perfil_escribano(request):
    return render(request, 'principal/perfil_escribano.html', context=None)

def resultado_busqueda(request):
    return render(request, 'principal/resultado_busqueda.html', context=None)