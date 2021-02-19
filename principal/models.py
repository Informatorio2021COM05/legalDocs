from django.db import models
from django.db.models.deletion import CASCADE


class Usuario(models.Model):
    usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Escribano(Usuario):
    matricula = models.IntegerField()
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    altura = models.IntegerField()
    piso = models.IntegerField(blank=True)
    numeroPuerta = models.CharField(max_length=5, blank=True)

class Cliente(Usuario):
    pass


class Turno(models.Model):
    idTurno = models.AutoField(primary_key=True)
    fecha = models.DateTimeField('%Y-%m-%d %H:%M')
    Escribano_id = models.ForeignKey(Escribano, on_delete=models.CASCADE)
    #Cliente_idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Cliente_id = models.OneToOneField(Cliente, on_delete=models.CASCADE)


class Documento(models.Model):
    paginas = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    doc = models.FileField(upload_to="documento", null=True)
    Cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Escribano_id = models.ForeignKey(Escribano, on_delete=models.CASCADE)