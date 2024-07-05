from django.db import models


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, verbose_name='ID del producto')
    categoria_producto = models.IntegerField(verbose_name='Categoría del producto')

    def __str__(self):
        return f"Producto ID: {self.id_producto}, Categoría: {self.categoria_producto}"

class DiscoDuro(models.Model):
    id_disco_duro = models.AutoField(primary_key=True, verbose_name='ID del disco duro')
    nombre_disco = models.CharField(max_length=50, verbose_name='Nombre del disco')
    valor_disco = models.PositiveIntegerField(verbose_name='Valor del disco')
    descripcion_disco = models.CharField(max_length=300, verbose_name='Descripción del disco')
    imagen_disco = models.CharField(max_length=250, verbose_name='Imagen del disco')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='discos_duros')

    def __str__(self):
        return self.nombre_disco

class Gabinete(models.Model):
    id_gabinete = models.AutoField(primary_key=True, verbose_name='ID del gabinete')
    nombre_gabinete = models.CharField(max_length=50, verbose_name='Nombre del gabinete')
    valor_gabinete = models.PositiveIntegerField(verbose_name='Valor del gabinete')
    descripcion_gabinete = models.CharField(max_length=500, verbose_name='Descripción del gabinete')
    imagen_gabinete = models.CharField(max_length=250, verbose_name='Imagen del gabinete')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='gabinetes')

    def __str__(self):
        return self.nombre_gabinete

class Procesador(models.Model):
    id_procesador = models.AutoField(primary_key=True, verbose_name='ID del procesador')
    nombre_procesador = models.CharField(max_length=50, verbose_name='Nombre del procesador')
    valor_procesador = models.PositiveIntegerField(verbose_name='Valor del procesador')
    descripcion_procesador = models.CharField(max_length=500, verbose_name='Descripción del procesador')
    imagen_procesador = models.CharField(max_length=250, verbose_name='Imagen del procesador')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='procesadores')

    def __str__(self):
        return self.nombre_procesador

class TarjetaVideo(models.Model):
    id_tarjeta_video = models.AutoField(primary_key=True, verbose_name='ID de la tarjeta de video')
    nombre_tarjeta_video = models.CharField(max_length=50, verbose_name='Nombre de la tarjeta de video')
    valor_tarjeta_video = models.PositiveIntegerField(verbose_name='Valor de la tarjeta de video')
    descripcion_tarjeta_video = models.CharField(max_length=500, verbose_name='Descripción de la tarjeta de video')
    imagen_tarjeta_video = models.CharField(max_length=250, verbose_name='Imagen de la tarjeta de video')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='tarjetas_video')

    def __str__(self):
        return self.nombre_tarjeta_video
