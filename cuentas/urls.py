from django.urls import path
from .views import SignUpView, SignUpSuccesfulView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('registro_exitoso', SignUpSuccesfulView.as_view(), name='registro_exitoso')
    #path('signup_escribano/', views.EscribanoSignup.register, name='signup_escribano'),
]