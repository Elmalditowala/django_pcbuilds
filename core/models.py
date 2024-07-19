from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

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
    imagen_disco = models.ImageField(upload_to='discosduros/', default='discosduros/default.jpg')

    def __str__(self):
        return self.nombre_disco
    
from django.db import models

class Gabinete(models.Model):
    id_gabinete = models.AutoField(primary_key=True, verbose_name='ID del gabinete')
    nombre_gabinete = models.CharField(max_length=50, verbose_name='Nombre del gabinete')
    valor_gabinete = models.PositiveIntegerField(verbose_name='Valor del gabinete')
    descripcion_gabinete = models.CharField(max_length=300, verbose_name='Descripción del gabinete')
    imagen_gabinete = models.ImageField(upload_to='gabinetes/', default='gabinetes/default.jpg')

    def __str__(self):
        return self.nombre_gabinete
    
class Procesador(models.Model):
    id_procesador = models.AutoField(primary_key=True, verbose_name='ID del procesador')
    nombre_procesador = models.CharField(max_length=50, verbose_name='Nombre del procesador')
    valor_procesador = models.PositiveIntegerField(verbose_name='Valor del procesador')
    descripcion_procesador = models.CharField(max_length=300, verbose_name='Descripción del procesador')
    imagen_procesador = models.ImageField(upload_to='procesadores/', default='procesadores/default.jpg')

    def __str__(self):
        return self.nombre_procesador
    
class TarjetaVideo(models.Model):
    id_tarjeta_video = models.AutoField(primary_key=True, verbose_name='ID de la tarjeta de video')
    nombre_tarjeta_video = models.CharField(max_length=50, verbose_name='Nombre de la tarjeta de video')
    valor_tarjeta_video = models.PositiveIntegerField(verbose_name='Valor de la tarjeta de video')
    descripcion_tarjeta_video = models.CharField(max_length=300, verbose_name='Descripción de la tarjeta de video')
    imagen_tarjeta_video = models.ImageField(upload_to='tarjetasvideo/', default='tarjetasvideo/default.jpg')

    def __str__(self):
        return self.nombre_tarjeta_video
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrito de {self.usuario.username}'

    @property
    def total(self):
        return sum(item.total for item in self.items.all())

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'

    @property
    def total(self):
        return self.cantidad * self.producto.precio
    

    



