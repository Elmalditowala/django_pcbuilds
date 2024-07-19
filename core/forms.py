from django import forms
from .models import UsuarioHardware

class RegistroForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Repetir Contraseña")

    class Meta:
        model = UsuarioHardware
        fields = ['nombre', 'apellidos', 'nombreUsuario', 'numero_telefonico', 'correo', 'contraseña', 'rol']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get('contraseña')
        password2 = cleaned_data.get('password2')

        if contraseña and password2 and contraseña != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data
    
class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioHardware
        fields = ['nombreUsuario', 'nombre', 'apellidos', 'numero_telefonico', 'correo', 'rol']

class RegistroUsuarioForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Repetir Contraseña")

    class Meta:
        model = UsuarioHardware
        fields = ['nombre', 'apellidos', 'nombreUsuario', 'numero_telefonico', 'correo', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get('contraseña')
        password2 = cleaned_data.get('password2')

        if contraseña and password2 and contraseña != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)