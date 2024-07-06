from django import forms
from .models import Producto, DiscoDuro, Gabinete, Procesador, TarjetaVideo

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class DiscoDuroForm(forms.ModelForm):
    class Meta:
        model = DiscoDuro
        fields = '__all__'

class GabineteForm(forms.ModelForm):
    class Meta:
        model = Gabinete
        fields = '__all__'

class ProcesadorForm(forms.ModelForm):
    class Meta:
        model = Procesador
        fields = '__all__'

class TarjetaVideoForm(forms.ModelForm):
    class Meta:
        model = TarjetaVideo
        fields = '__all__'
