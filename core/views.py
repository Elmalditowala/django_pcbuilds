from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from .models import Producto, DiscoDuro, Gabinete, Procesador, TarjetaVideo
from .forms import ProductoForm, DiscoDuroForm, GabineteForm, ProcesadorForm, TarjetaVideoForm

# Admin index view
class AdminIndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'admin/indexadmin.html')

# Manage Views
class ProductoManageView(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        if 'edit' in request.GET:
            instance = get_object_or_404(Producto, pk=pk)
            form = ProductoForm(instance=instance)
            return render(request, 'admin/product_manage.html', {'form': form, 'edit': True})
        elif 'delete' in request.GET:
            instance = get_object_or_404(Producto, pk=pk)
            if request.method == 'POST':
                instance.delete()
                return redirect('producto_manage')
            return render(request, 'admin/product_manage.html', {'instance': instance, 'delete': True})
        else:
            form = ProductoForm()
            items = Producto.objects.all()
            return render(request, 'admin/product_manage.html', {'form': form, 'items': items})

    def post(self, request, pk=None):
        if pk:
            instance = get_object_or_404(Producto, pk=pk)
            form = ProductoForm(request.POST, instance=instance)
        else:
            form = ProductoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('producto_manage')
        return render(request, 'admin/product_manage.html', {'form': form})

class DiscoDuroManageView(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        if 'edit' in request.GET:
            instance = get_object_or_404(DiscoDuro, pk=pk)
            form = DiscoDuroForm(instance=instance)
            return render(request, 'admin/disco_duro_manage.html', {'form': form, 'edit': True})
        elif 'delete' in request.GET:
            instance = get_object_or_404(DiscoDuro, pk=pk)
            if request.method == 'POST':
                instance.delete()
                return redirect('disco_duro_manage')
            return render(request, 'admin/disco_duro_manage.html', {'instance': instance, 'delete': True})
        else:
            form = DiscoDuroForm()
            items = DiscoDuro.objects.all()
            return render(request, 'admin/disco_duro_manage.html', {'form': form, 'items': items})

    def post(self, request, pk=None):
        if pk:
            instance = get_object_or_404(DiscoDuro, pk=pk)
            form = DiscoDuroForm(request.POST, instance=instance)
        else:
            form = DiscoDuroForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('disco_duro_manage')
        return render(request, 'admin/disco_duro_manage.html', {'form': form})

class GabineteManageView(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        if 'edit' in request.GET:
            instance = get_object_or_404(Gabinete, pk=pk)
            form = GabineteForm(instance=instance)
            return render(request, 'admin/gabinete_manage.html', {'form': form, 'edit': True})
        elif 'delete' in request.GET:
            instance = get_object_or_404(Gabinete, pk=pk)
            if request.method == 'POST':
                instance.delete()
                return redirect('gabinete_manage')
            return render(request, 'admin/gabinete_manage.html', {'instance': instance, 'delete': True})
        else:
            form = GabineteForm()
            items = Gabinete.objects.all()
            return render(request, 'admin/gabinete_manage.html', {'form': form, 'items': items})

    def post(self, request, pk=None):
        if pk:
            instance = get_object_or_404(Gabinete, pk=pk)
            form = GabineteForm(request.POST, instance=instance)
        else:
            form = GabineteForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('gabinete_manage')
        return render(request, 'admin/gabinete_manage.html', {'form': form})

class ProcesadorManageView(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        if 'edit' in request.GET:
            instance = get_object_or_404(Procesador, pk=pk)
            form = ProcesadorForm(instance=instance)
            return render(request, 'admin/procesador_manage.html', {'form': form, 'edit': True})
        elif 'delete' in request.GET:
            instance = get_object_or_404(Procesador, pk=pk)
            if request.method == 'POST':
                instance.delete()
                return redirect('procesador_manage')
            return render(request, 'admin/procesador_manage.html', {'instance': instance, 'delete': True})
        else:
            form = ProcesadorForm()
            items = Procesador.objects.all()
            return render(request, 'admin/procesador_manage.html', {'form': form, 'items': items})

    def post(self, request, pk=None):
        if pk:
            instance = get_object_or_404(Procesador, pk=pk)
            form = ProcesadorForm(request.POST, instance=instance)
        else:
            form = ProcesadorForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('procesador_manage')
        return render(request, 'admin/procesador_manage.html', {'form': form})

class TarjetaVideoManageView(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        if 'edit' in request.GET:
            instance = get_object_or_404(TarjetaVideo, pk=pk)
            form = TarjetaVideoForm(instance=instance)
            return render(request, 'admin/tarjeta_video_manage.html', {'form': form, 'edit': True})
        elif 'delete' in request.GET:
            instance = get_object_or_404(TarjetaVideo, pk=pk)
            if request.method == 'POST':
                instance.delete()
                return redirect('tarjeta_video_manage')
            return render(request, 'admin/tarjeta_video_manage.html', {'instance': instance, 'delete': True})
        else:
            form = TarjetaVideoForm()
            items = TarjetaVideo.objects.all()
            return render(request, 'admin/tarjeta_video_manage.html', {'form': form, 'items': items})

    def post(self, request, pk=None):
        if pk:
            instance = get_object_or_404(TarjetaVideo, pk=pk)
            form = TarjetaVideoForm(request.POST, instance=instance)
        else:
            form = TarjetaVideoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('tarjeta_video_manage')
        return render(request, 'admin/tarjeta_video_manage.html', {'form': form})

# Páginas públicas
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
