
from django.urls import path, include
from .views import *

app_name = 'admon'
urlpatterns=[
	path('index/', index, name='index'),

	path('iniciarSesion', iniciarSesion, name='inicarsesion'),
	path('autenticarUsuario', autenticarUsuario, name='autenticar_usuario'),
	path('cerrarSesion', cerrarSesion, name='cerrar_sesion'),
	path('bienvenida', bienvenida, name='bienvenida'),
	path('gestionEstudiante/', ListadoEstudiante.as_view(), name='listado_estudiante'),
	path('matricula/', crearEstudiante.as_view(), name='crear_estudiante'),
	
	]