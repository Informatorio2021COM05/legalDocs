from django.urls import path
from . import views

app_name = 'principal'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('validar_documento/', views.validar_documento, name='validar_documento'),
    path('cargar_documento/', views.cargar_documento, name='cargar_documento'),
    path('buscador_escribano/', views.BuscadorView.as_view(), name='buscador_escribano'),
    path('perfil_cliente/', views.perfil_cliente, name='perfil_cliente'),
    path('editar_cliente/<int:pk>', views.EditarClienteView.as_view(), name = 'editar_cliente'),
    path('detalle_escribano/<int:pk>', views.DetalleEscribanoView.as_view(), name='detalle_escribano'),
    path('perfil_escribano/', views.perfil_escribano, name='perfil_escribano'),
    path('resultado_busqueda/', views.resultado_busqueda, name='resultado_busqueda'),
]