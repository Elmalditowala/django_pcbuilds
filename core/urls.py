from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    fichacomponentes, index, prearmados, carrito, contacto, discoduro, discossd, fichapc, gabinetes, memoriasram, pagoaprobado, placasmadres, politicadereembolso, procesadores, quienessomos, software, tarjetasdevideo, terminoycondiciones,
    AdminIndexView, ProductoManageView, DiscoDuroManageView, GabineteManageView, ProcesadorManageView, TarjetaVideoManageView
)

urlpatterns = [
    path('', index, name="index"),
    path('prearmados', prearmados, name="prearmados"),
    path('carrito', carrito, name="carrito"),
    path('contacto', contacto, name="contacto"),
    path('discoduro', discoduro, name="discoduro"),
    path('discossd', discossd, name="discossd"),
    path('fichacomponentes', fichacomponentes, name="fichacomponentes"),
    path('fichapc', fichapc, name="fichapc"),
    path('gabinetes', gabinetes, name="gabinetes"),
    path('memoriasram', memoriasram, name="memoriasram"),
    path('pagoaprobado', pagoaprobado, name="pagoaprobado"),
    path('placasmadres', placasmadres, name="placasmadres"),
    path('politicadereembolso', politicadereembolso, name="politicadereembolso"),
    path('procesadores', procesadores, name="procesadores"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('software', software, name="software"),
    path('tarjetasdevideo', tarjetasdevideo, name="tarjetasdevideo"),
    path('terminoycondiciones', terminoycondiciones, name="terminoycondiciones"),

    # ulr para los crud
    path('admin/', AdminIndexView.as_view(), name='admin_index'),
    path('admin/productos/', ProductoManageView.as_view(), name='producto_manage'),
    path('admin/productos/<int:pk>/', ProductoManageView.as_view(), name='producto_manage'),
    path('admin/discos-duros/', DiscoDuroManageView.as_view(), name='disco_duro_manage'),
    path('admin/discos-duros/<int:pk>/', DiscoDuroManageView.as_view(), name='disco_duro_manage'),
    path('admin/gabinetes/', GabineteManageView.as_view(), name='gabinete_manage'),
    path('admin/gabinetes/<int:pk>/', GabineteManageView.as_view(), name='gabinete_manage'),
    path('admin/procesadores/', ProcesadorManageView.as_view(), name='procesador_manage'),
    path('admin/procesadores/<int:pk>/', ProcesadorManageView.as_view(), name='procesador_manage'),
    path('admin/tarjetas-video/', TarjetaVideoManageView.as_view(), name='tarjeta_video_manage'),
    path('admin/tarjetas-video/<int:pk>/', TarjetaVideoManageView.as_view(), name='tarjeta_video_manage'),

    # urlsextra
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
