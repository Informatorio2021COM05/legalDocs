from django.urls import path
from .views import SignUpView, SignUpSuccesfulView, EscribanoSignUpView
from cuentas.views import EditarUsuarioView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup_escribano/', EscribanoSignUpView.as_view(), name='escribano_signup'),
    path('registro_exitoso', SignUpSuccesfulView.as_view(), name='registro_exitoso'),
    #path('signup_escribano/', views.EscribanoSignup.register, name='signup_escribano'),
    path('editar_perfil/<int:pk>', EditarUsuarioView.as_view(), name= 'editar_perfil'),
]