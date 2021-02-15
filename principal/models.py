from django.db import models
from django.db.models.deletion import CASCADE


class Usuarios(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    email = models.EmailField(max_length=100)
    contrasenia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Escribano(Usuarios):
    idEscribano = models.AutoField(primary_key=True)
    matricula = models.IntegerField()
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    calle = models.CharField(max_length=100)
    altura = models.IntegerField()
    piso = models.IntegerField(blank=True)
    numeroPuerta = models.CharField(max_length=5, blank=True)

class Cliente(Usuarios):
    idCliente = models.AutoField(primary_key=True)

class Turno(models.Model):
    idTurno = models.AutoField(primary_key=True)
    fecha = models.DateTimeField('%Y-%m-%d %H:%M')
    Escribano_idEscribano = models.ForeignKey(Escribano, on_delete=models.CASCADE)
    #Cliente_idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Cliente_idCliente = models.OneToOneField(Cliente, on_delete=CASCADE)


class Documento(models.Model):
    idDocumento = models.AutoField(primary_key=True)
    paginas = models.IntegerField()
    tipo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="documento")
    Cliente_idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Escribano_idEscribano = models.ForeignKey(Escribano, on_delete=models.CASCADE)l