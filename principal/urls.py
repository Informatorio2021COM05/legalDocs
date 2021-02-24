from django.urls import path
from . import views

app_name = 'principal'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('validar/', views.validar, name='validar'),
    path('buscador_escribano/', views.BuscadorView.as_view(), name='buscador_escribano'),
    path('detalle_perfil/', views.perfil_cliente, name='detalle_perfil'),
    path('editar_perfil/<int:pk>', views.EditarUsuarioView.as_view(), name= 'editar_perfil'),
    path('detalle_escribano/<int:pk>', views.DetalleEscribanoView.as_view(), name='detalle_escribano'),
    path('cargar_documento/', views.CargarDocumentoView.as_view(), name= 'cargar_documento'),
    path('<slug:slug>/', views.DetalleDocumentoView.as_view(), name= 'detalle_documento'),
    path('<slug:slug>/editar_documento', views.EditarDocumentoView.as_view(), name= 'editar_documento'),
]