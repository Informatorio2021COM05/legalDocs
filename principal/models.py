from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from cuentas.models import CustomUser, Escribano


class Turno(models.Model):
    fecha = models.DateTimeField('%Y-%m-%d %H:%M')
    Escribano_id = models.ForeignKey(Escribano, on_delete=models.CASCADE, related_name='+')
    #Cliente_idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Cliente_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fecha

class Documento(models.Model):
    paginas = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=100)
    archivo = models.FileField(upload_to="documentos", null=True)
    Cliente_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')
    Escribano_id = models.ForeignKey(Escribano, on_delete=models.CASCADE, )

    def __str__(self):
        return self.descripcion