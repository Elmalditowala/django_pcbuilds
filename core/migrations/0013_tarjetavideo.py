# Generated by Django 5.0.6 on 2024-07-19 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_procesador'),
    ]

    operations = [
        migrations.CreateModel(
            name='TarjetaVideo',
            fields=[
                ('id_tarjeta_video', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la tarjeta de video')),
                ('nombre_tarjeta_video', models.CharField(max_length=50, verbose_name='Nombre de la tarjeta de video')),
                ('valor_tarjeta_video', models.PositiveIntegerField(verbose_name='Valor de la tarjeta de video')),
                ('descripcion_tarjeta_video', models.CharField(max_length=300, verbose_name='Descripción de la tarjeta de video')),
                ('imagen_tarjeta_video', models.ImageField(default='tarjetasvideo/default.jpg', upload_to='tarjetasvideo/')),
            ],
        ),
    ]
