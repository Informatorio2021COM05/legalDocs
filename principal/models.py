from django.db import models, IntegrityError
from django.db.models.deletion import CASCADE
from cuentas.models import CustomUser
from django.utils.crypto import get_random_string
from django.urls import reverse


class Turno(models.Model):
    fecha = models.DateField('fecha', null=True, blank=True)
    hora = models.TimeField('hora', null=True, blank=True)
    escribano = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fecha



class Documento(models.Model):
    titulo = models.CharField(max_length=50, verbose_name= 'Título')
    descripcion = models.CharField(max_length=300, default='', blank=True, verbose_name= 'Descripción')
    paginas = models.PositiveIntegerField(verbose_name= 'Cantidad de páginas')
    archivo = models.FileField(upload_to="documentos/", blank=True, null=True, verbose_name= 'Archivo')
    slug = models.CharField(max_length=4, blank=True, editable=False, unique=True, verbose_name= 'Código de identificación')
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+', verbose_name= 'Cliente')
    escribano = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('principal:detalle_documento', args=[str(self.slug)])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_random_string(length=4) + '-' + get_random_string(length=4)
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
                    self.slug = get_random_string(length=4) + '-' + get_random_string(length=4)
            else:
                success = True