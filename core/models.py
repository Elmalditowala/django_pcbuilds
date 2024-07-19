from django.db import models
from django.contrib.auth.hashers import make_password

class RolHardware(models.Model):
    idRol = models.AutoField(primary_key=True, verbose_name='Id rol')
    nombreRol = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.idRol} {self.nombreRol}"

class UsuarioHardware(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name='Id de usuario')
    nombreUsuario = models.CharField(max_length=15)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    numero_telefonico = models.CharField(max_length=20, verbose_name="Número Telefónico (+56)", default='0000000000')
    correo = models.EmailField(max_length=40)
    contraseña = models.CharField(max_length=128)
    fechacreacion = models.DateField(verbose_name='Fecha de creación', auto_now_add=True)
    rol = models.ForeignKey(RolHardware, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.contraseña = make_password(self.contraseña)
        super(UsuarioHardware, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.idUsuario} {self.nombreUsuario}"

