from django.urls import path
from .views import SignUpView, SignUpSuccesfulView, EscribanoSignUpView, PerfilUsuario
from cuentas.views import EditarUsuarioView


app_name = 'cuentas'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup_escribano/', EscribanoSignUpView.as_view(), name='escribano_signup'),
    path('registro_exitoso', SignUpSuccesfulView.as_view(), name='registro_exitoso'),
    path('perfil/<int:pk>', PerfilUsuario.as_view(), name= 'perfil'),
    path('editar_perfil/<int:pk>', EditarUsuarioView.as_view(), name= 'editar_perfil'),
]