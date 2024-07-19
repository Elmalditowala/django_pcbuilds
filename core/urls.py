from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    fichacomponentes, index, prearmados, carrito, contacto, discoduro, discossd, fichapc, gabinetes, memoriasram, pagoaprobado, placasmadres, politicadereembolso, procesadores, quienessomos, 
    software, tarjetasdevideo, terminoycondiciones, indexadmin,registrar_usuario_admin,listar_usuarios,editar_usuario,borrar_usuario,registrar_usuario,iniciar_sesion
)

urlpatterns = [
    path('', index, name="index"),
    path('prearmados/', prearmados, name="prearmados"),
    path('carrito/', carrito, name="carrito"),
    path('contacto/', contacto, name="contacto"),
    path('discoduro/', discoduro, name="discoduro"),
    path('discossd/', discossd, name="discossd"),
    path('fichacomponentes/', fichacomponentes, name="fichacomponentes"),
    path('fichapc/', fichapc, name="fichapc"),
    path('gabinetes/', gabinetes, name="gabinetes"),
    path('memoriasram/', memoriasram, name="memoriasram"),
    path('pagoaprobado/', pagoaprobado, name="pagoaprobado"),
    path('placasmadres/', placasmadres, name="placasmadres"),
    path('politicadereembolso/', politicadereembolso, name="politicadereembolso"),
    path('procesadores/', procesadores, name="procesadores"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('software/', software, name="software"),
    path('tarjetasdevideo/', tarjetasdevideo, name="tarjetasdevideo"),
    path('terminoycondiciones/', terminoycondiciones, name="terminoycondiciones"),
    

    # URLs para los CRUDs de administración

    path('indexadmin/', indexadmin, name="indexadmin"),
    path('registrar_usuario/', registrar_usuario_admin, name='registrar_usuario_admin'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('editar_usuario/<int:usuario_id>/', editar_usuario, name='editar_usuario'),
    path('borrar_usuario/<int:usuario_id>/', borrar_usuario, name='borrar_usuario'),


    # URLs para los CRUDs de registro e inicio de sesion usuario

    path('registrar/',registrar_usuario, name='registrar_usuario'),
    path('iniciar_sesion/',iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', LogoutView.as_view(next_page='iniciar_sesion'), name='cerrar_sesion'),
]