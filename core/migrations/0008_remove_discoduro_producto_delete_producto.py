# Generated by Django 5.0.6 on 2024-07-19 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_discoduro_imagen_disco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discoduro',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
