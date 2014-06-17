from django.conf.urls import patterns, include, url
from views import *
urlpatterns = patterns('',

	#url(r'^$', Login),
	url(r'^$', menu),
	url(r'^db/menu/$',menu),
	url(r'^db/cerrarsesion/$',cerrar_sesion),
	url(r'^db/password_nuevo/$',password_nuevo),
	url(r'^db/new/usuario/$',nuevo_usuario),
	url(r'^db/menu/sugerenciaslink/',sugerencia),
	url(r'^db/menu/turismolink/',la_pazView),
	url(r'^db/menu/reservaslink/',reservasView),
	url(r'^db/menu/ventaslink/',ventasView),
	url(r'^db/menu/ciudades/orurolink/',oruroView),
	url(r'^db/menu/ciudades/potosilink/',potosiView),
	url(r'^db/menu/ciudades/cochabambalink/',cochabambaView),
	url(r'^db/menu/ciudades/santa_cruzlink/',santa_cruzView),
	url(r'^db/menu/loginlink/',iniciar_sessionView),
	url(r'^db/menu/rutaslink/',rutasView),
	url(r'^db/menu/buseslink/',busView),
	url(r'^db/menu/usuarioslink/',usuariosView),
	url(r'^db/menu/salidaslink/',salidasView),

)