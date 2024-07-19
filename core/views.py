from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View
from .models import UsuarioHardware, RolHardware
from .forms import RegistroForm,RegistroUsuarioForm,LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login


# Vistas públicas
def index(request):
    return render(request, 'core/index.html')

def prearmados(request):
    return render(request, 'core/pre-armados.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def discoduro(request):
    return render(request, 'core/discoduro.html')

def discossd(request):
    return render(request, 'core/discossd.html')

def fichacomponentes(request):
    return render(request, 'core/fichacomponentes.html')

def fichapc(request):
    return render(request, 'core/fichapc.html')

def gabinetes(request):
    return render(request, 'core/gabinetes.html')

def memoriasram(request):
    return render(request, 'core/memorias-ram.html')

def pagoaprobado(request):
    return render(request, 'core/pagoaprobado.html')

def placasmadres(request):
    return render(request, 'core/placas-madres.html')

def politicadereembolso(request):
    return render(request, 'core/politica-de-reembolso.html')

def procesadores(request):
    return render(request, 'core/procesadores.html')

def quienessomos(request):
    return render(request, 'core/quienes-somos.html')

def software(request):
    return render(request, 'core/software.html')

def tarjetasdevideo(request):
    return render(request, 'core/tarjetasdevideo.html')

def terminoycondiciones(request):
    return render(request, 'core/termino-y-condiciones.html')

# Vista Admin Index
def indexadmin(request):
    usuarios = UsuarioHardware.objects.all()
    return render(request, 'admin/indexadmin.html', {'usuarios': usuarios})


# Vista para registrar usuarios admin
def registrar_usuario_admin(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.contraseña = make_password(form.cleaned_data.get('contraseña'))
            usuario.save()
            return redirect('indexadmin')  
    else:
        form = RegistroForm()
    roles = RolHardware.objects.all()
    return render(request, 'admin/crear_usuario.html', {'form': form, 'roles': roles})

# Vista para listar usuarios
def listar_usuarios(request):
    usuarios = UsuarioHardware.objects.all()
    return render(request, 'admin/listar_usuarios.html', {'usuarios': usuarios})

# Vista para editar usuarios
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(UsuarioHardware, idUsuario=usuario_id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.contraseña = make_password(form.cleaned_data.get('contraseña'))
            usuario.save()
            return redirect('listar_usuarios')
    else:
        form = RegistroForm(instance=usuario)
    return render(request, 'admin/editar_usuario.html', {'form': form, 'usuario': usuario})

# Vista para borrar usuarios
def borrar_usuario(request, usuario_id):
    usuario = get_object_or_404(UsuarioHardware, idUsuario=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'admin/borrar_usuario.html', {'usuario': usuario})

# Vista para crear usuarios
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.rol_id = 2  # Asigna el rol de usuario por ID
            user.save()
            return redirect('index')  
    else:
        form = RegistroUsuarioForm()
    return render(request, 'core/registro_usuario.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') 
            else:
                return render(request, 'core/iniciar_sesion.html', {'form': form, 'error': 'Credenciales inválidas'})
    else:
        form = LoginForm()
    return render(request, 'core/iniciar_sesion.html', {'form': form})
