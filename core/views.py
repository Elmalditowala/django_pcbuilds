from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View
from .models import UsuarioHardware, RolHardware,DiscoDuro,Gabinete,Procesador,TarjetaVideo
from .forms import RegistroForm,RegistroUsuarioForm,LoginForm,DiscoDuroForm,GabineteForm,ProcesadorForm,TarjetaVideoForm
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


def listar_discos_duros(request):
    discos_duros = DiscoDuro.objects.all()
    return render(request, 'admin/listar_discos_duros.html', {'discos_duros': discos_duros})

def agregar_disco_duro(request):
    if request.method == 'POST':
        form = DiscoDuroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_discos_duros')
    else:
        form = DiscoDuroForm()
    return render(request, 'admin/agregar_disco_duro.html', {'form': form})

def editar_disco_duro(request, pk):
    disco_duro = get_object_or_404(DiscoDuro, pk=pk)
    if request.method == 'POST':
        form = DiscoDuroForm(request.POST, request.FILES, instance=disco_duro)
        if form.is_valid():
            form.save()
            return redirect('listar_discos_duros')
    else:
        form = DiscoDuroForm(instance=disco_duro)
    return render(request, 'admin/editar_disco_duro.html', {'form': form})

def borrar_disco_duro(request, pk):
    disco_duro = get_object_or_404(DiscoDuro, pk=pk)
    if request.method == 'POST':
        disco_duro.delete()
        return redirect('listar_discos_duros')
    return render(request, 'admin/borrar_disco_duro.html', {'disco_duro': disco_duro})


# Listar gabinetes
def listar_gabinetes(request):
    gabinetes = Gabinete.objects.all()
    return render(request, 'admin/listar_gabinetes.html', {'gabinetes': gabinetes})

# Agregar gabinete
def agregar_gabinete(request):
    if request.method == 'POST':
        form = GabineteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_gabinetes')
    else:
        form = GabineteForm()
    return render(request, 'admin/agregar_gabinete.html', {'form': form})

# Editar gabinete
def editar_gabinete(request, pk):
    gabinete = get_object_or_404(Gabinete, pk=pk)
    if request.method == 'POST':
        form = GabineteForm(request.POST, request.FILES, instance=gabinete)
        if form.is_valid():
            form.save()
            return redirect('listar_gabinetes')
    else:
        form = GabineteForm(instance=gabinete)
    return render(request, 'admin/editar_gabinete.html', {'form': form})

# Borrar gabinete
def borrar_gabinete(request, pk):
    gabinete = get_object_or_404(Gabinete, pk=pk)
    if request.method == 'POST':
        gabinete.delete()
        return redirect('listar_gabinetes')
    return render(request, 'admin/borrar_gabinete.html', {'gabinete': gabinete})


# Listar procesadores
def listar_procesadores(request):
    procesadores = Procesador.objects.all()
    return render(request, 'admin/listar_procesadores.html', {'procesadores': procesadores})

# Agregar procesador
def agregar_procesador(request):
    if request.method == 'POST':
        form = ProcesadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_procesadores')
    else:
        form = ProcesadorForm()
    return render(request, 'admin/agregar_procesador.html', {'form': form})

# Editar procesador
def editar_procesador(request, pk):
    procesador = get_object_or_404(Procesador, pk=pk)
    if request.method == 'POST':
        form = ProcesadorForm(request.POST, request.FILES, instance=procesador)
        if form.is_valid():
            form.save()
            return redirect('listar_procesadores')
    else:
        form = ProcesadorForm(instance=procesador)
    return render(request, 'admin/editar_procesador.html', {'form': form})

# Borrar procesador
def borrar_procesador(request, pk):
    procesador = get_object_or_404(Procesador, pk=pk)
    if request.method == 'POST':
        procesador.delete()
        return redirect('listar_procesadores')
    return render(request, 'admin/borrar_procesador.html', {'procesador': procesador})

# Listar tarjetas de video
def listar_tarjetas_video(request):
    tarjetas_video = TarjetaVideo.objects.all()
    return render(request, 'admin/listar_tarjetas_video.html', {'tarjetas_video': tarjetas_video})

# Agregar tarjeta de video
def agregar_tarjeta_video(request):
    if request.method == 'POST':
        form = TarjetaVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_tarjetas_video')
    else:
        form = TarjetaVideoForm()
    return render(request, 'admin/agregar_tarjeta_video.html', {'form': form})

# Editar tarjeta de video
def editar_tarjeta_video(request, pk):
    tarjeta_video = get_object_or_404(TarjetaVideo, pk=pk)
    if request.method == 'POST':
        form = TarjetaVideoForm(request.POST, request.FILES, instance=tarjeta_video)
        if form.is_valid():
            form.save()
            return redirect('listar_tarjetas_video')
    else:
        form = TarjetaVideoForm(instance=tarjeta_video)
    return render(request, 'admin/editar_tarjeta_video.html', {'form': form})

# Borrar tarjeta de video
def borrar_tarjeta_video(request, pk):
    tarjeta_video = get_object_or_404(TarjetaVideo, pk=pk)
    if request.method == 'POST':
        tarjeta_video.delete()
        return redirect('listar_tarjetas_video')
    return render(request, 'admin/borrar_tarjeta_video.html', {'tarjeta_video': tarjeta_video})
