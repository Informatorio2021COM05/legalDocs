from django.urls import path

from . import views

app_name = 'principal'
urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('validar_documento/', views.validar_documento, name='validar_documento'),
    path('cargar_documento/', views.cargar_documento, name='cargar_documento'),
    path('buscador_escribano/', views.buscador_escribano, name='buscador_escribano'),
    path('perfil_cliente/', views.perfil_cliente, name='perfil_cliente'),
    path('perfil_escribano_desde_usuario/', views.perfil_escribano_desde_usuario, name='perfil_escribano_desde_usuario'),
    path('perfil_escribano/', views.perfil_escribano, name='perfil_escribano'),
    path('resultado_busqueda/', views.resultado_busqueda, name='resultado_busqueda'),

]