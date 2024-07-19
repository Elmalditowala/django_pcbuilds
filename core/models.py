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
    

class DiscoDuro(models.Model):
    id_disco_duro = models.AutoField(primary_key=True, verbose_name='ID del disco duro')
    nombre_disco = models.CharField(max_length=50, verbose_name='Nombre del disco')
    valor_disco = models.PositiveIntegerField(verbose_name='Valor del disco')
    descripcion_disco = models.CharField(max_length=300, verbose_name='Descripción del disco')
    imagen_disco = models.ImageField(upload_to='discosduros/')

    def __str__(self):
        return self.nombre_disco



