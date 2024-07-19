from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import (
    fichacomponentes, index, prearmados, carrito, contacto, discoduro, discossd, fichapc, gabinetes, memoriasram, pagoaprobado, placasmadres, politicadereembolso, procesadores, quienessomos, 
    software, tarjetasdevideo, terminoycondiciones, indexadmin,registrar_usuario_admin,listar_usuarios,editar_usuario,borrar_usuario,registrar_usuario,iniciar_sesion,
    listar_discos_duros,editar_disco_duro,agregar_disco_duro,borrar_disco_duro,listar_gabinetes,agregar_gabinete,editar_gabinete,borrar_gabinete,
    listar_procesadores,agregar_procesador,editar_procesador,borrar_procesador,listar_tarjetas_video,agregar_tarjeta_video,editar_tarjeta_video,borrar_tarjeta_video
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

    # URLs para los CRUDs de Disco duro
    path('discos_duros/',listar_discos_duros, name='listar_discos_duros'),
    path('discos_duros/agregar/',agregar_disco_duro, name='agregar_disco_duro'),
    path('discos_duros/editar/<int:pk>/',editar_disco_duro, name='editar_disco_duro'),
    path('discos_duros/borrar/<int:pk>/',borrar_disco_duro, name='borrar_disco_duro'),

    # URLs para CRUDs Gabinete
    path('listar_gabinetes/',listar_gabinetes, name='listar_gabinetes'),
    path('gabinetes/agregar/',agregar_gabinete, name='agregar_gabinete'),
    path('gabinetes/editar/<int:pk>/',editar_gabinete, name='editar_gabinete'),
    path('gabinetes/borrar/<int:pk>/',borrar_gabinete, name='borrar_gabinete'),

     # URLs para Procesador
    path('listar_procesadores/',listar_procesadores, name='listar_procesadores'),
    path('procesadores/agregar/',agregar_procesador, name='agregar_procesador'),
    path('procesadores/editar/<int:pk>/',editar_procesador, name='editar_procesador'),
    path('procesadores/borrar/<int:pk>/',borrar_procesador, name='borrar_procesador'),

    # URLs para Tarjeta de Video
    path('listar_tarjetas_video/',listar_tarjetas_video, name='listar_tarjetas_video'),
    path('tarjetas_video/agregar/',agregar_tarjeta_video, name='agregar_tarjeta_video'),
    path('tarjetas_video/editar/<int:pk>/',editar_tarjeta_video, name='editar_tarjeta_video'),
    path('tarjetas_video/borrar/<int:pk>/',borrar_tarjeta_video, name='borrar_tarjeta_video'),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
