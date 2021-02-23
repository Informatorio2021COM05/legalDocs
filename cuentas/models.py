from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    dni = models.PositiveIntegerField(null=True)
    is_escribano = models.BooleanField(default=False)
    
    def __str__(self):
        return self.apellido + " " + self.nombre
    
    def get_absolute_url(self):
        return reverse('principal:detalle_perfil', args=[str(self.id)])


class Escribano(models.Model):
    customuser_ptr = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    matricula = models.IntegerField(null=True, blank=True)
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    altura = models.IntegerField()
    piso = models.IntegerField(null=True, blank=True)
    numeroPuerta = models.CharField(max_length=4, blank=True, default= '')