# Generated by Django 5.0.6 on 2024-07-19 04:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_usuariohardware_custom_user_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del producto')),
                ('categoria_producto', models.IntegerField(verbose_name='Categoría del producto')),
            ],
        ),
        migrations.CreateModel(
            name='DiscoDuro',
            fields=[
                ('id_disco_duro', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del disco duro')),
                ('nombre_disco', models.CharField(max_length=50, verbose_name='Nombre del disco')),
                ('valor_disco', models.PositiveIntegerField(verbose_name='Valor del disco')),
                ('descripcion_disco', models.CharField(max_length=300, verbose_name='Descripción del disco')),
                ('imagen_disco', models.CharField(max_length=250, verbose_name='Imagen del disco')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discos_duros', to='core.producto')),
            ],
        ),
    ]
