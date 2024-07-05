from django.contrib import admin
from .models import Producto,DiscoDuro,Gabinete,Procesador,TarjetaVideo

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'categoria_producto')
    search_fields = ('categoria_producto',)

class DiscoDuroAdmin(admin.ModelAdmin):
    list_display = ('id_disco_duro', 'nombre_disco', 'valor_disco', 'descripcion_disco', 'producto')
    search_fields = ('nombre_disco', 'producto__categoria_producto')

class GabineteAdmin(admin.ModelAdmin):
    list_display = ('id_gabinete', 'nombre_gabinete', 'valor_gabinete', 'descripcion_gabinete', 'producto')
    search_fields = ('nombre_gabinete', 'producto__categoria_producto')

class ProcesadorAdmin(admin.ModelAdmin):
    list_display = ('id_procesador', 'nombre_procesador', 'valor_procesador', 'descripcion_procesador', 'producto')
    search_fields = ('nombre_procesador', 'producto__categoria_producto')

class TarjetaVideoAdmin(admin.ModelAdmin):
    list_display = ('id_tarjeta_video', 'nombre_tarjeta_video', 'valor_tarjeta_video', 'descripcion_tarjeta_video', 'producto')
    search_fields = ('nombre_tarjeta_video', 'producto__categoria_producto')
    
admin.site.register(Producto)
admin.site.register(DiscoDuro)
admin.site.register(Gabinete)
admin.site.register(Procesador)
admin.site.register(TarjetaVideo)