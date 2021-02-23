from django.urls import path
from . import views

app_name = 'principal'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('validar_documento/', views.validar_documento, name='validar_documento'),
    path('cargar_documento/', views.cargar_documento, name='cargar_documento'),
    path('buscador_escribano/', views.BuscadorView.as_view(), name='buscador_escribano'),
    path('detalle_perfil/', views.perfil_cliente, name='detalle_perfil'),
    path('editar_perfil/<int:pk>', views.EditarUsuarioView.as_view(), name= 'editar_perfil'),
    path('detalle_escribano/<int:pk>', views.DetalleEscribanoView.as_view(), name='detalle_escribano'),
    path('resultado_busqueda/', views.resultado_busqueda, name='resultado_busqueda'),
    path('crear_documento/', views.CrearDocumentoView.as_view(), name= 'crear_documento'),
    path('<slug:codigo>/', views.DetalleDocumentoView.as_view(), name= 'detalle_documento'),
    path('creacion_documento_exitosa/', views.CreacionSuccessfulView.as_view(), name= 'creacion_doc_exitosa')
]