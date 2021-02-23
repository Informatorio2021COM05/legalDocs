from django.db import models, IntegrityError
from django.db.models.deletion import CASCADE
from cuentas.models import CustomUser, Escribano
from django.utils.crypto import get_random_string
from django.urls import reverse


class Turno(models.Model):
    fecha = models.DateTimeField('%Y-%m-%d %H:%M')
    Escribano_id = models.ForeignKey(Escribano, on_delete=models.CASCADE, related_name='+')
    #Cliente_idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Cliente_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fecha



class Documento(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300, default='', blank=True)
    paginas = models.PositiveIntegerField()
    archivo = models.FileField(upload_to="documentos/")
    slug = models.CharField(max_length=4, blank=True, editable=False, unique=True)
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')
    escribano = models.ForeignKey(Escribano, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('detalle_documento', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_random_string(length=4)
        success = False
        failures = 0
        while not success:
            try:
                super(Documento, self).save(*args, **kwargs)
            except IntegrityError:
                failures += 1
                if failures > 5:
                    raise
                else:
                    self.slug = get_random_string(length=4)
            else:
                success = True