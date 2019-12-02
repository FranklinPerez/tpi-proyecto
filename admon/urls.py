from .ajax import load_Docentes
from django.urls import path, include, re_path
from .views import *

app_name = 'admon'
urlpatterns=[
	path('index/', index, name='index'),

	path('iniciarSesion', iniciarSesion, name='inicar_sesion'),
	path('autenticarUsuario', autenticarUsuario, name='autenticar_usuario'),
	path('cerrarSesion', cerrarSesion, name='cerrar_sesion'),
	path('bienvenida', bienvenida, name='bienvenida'),
	path('gestionEstudiante/', ListadoEstudiante.as_view(), name='listado_estudiante'),
	path('matricula/', crearEstudiante.as_view(), name='crear_estudiante'),



















































	


	path('armarEvaluacion/', armarEvaluacion.as_view(), name='armarEvaluacion'),
	path('ajax/load_Docentes/', load_Docentes, name='load_Docentes'),
	path('evArmada', evArmada, name='armada'),
	path('gestionEvaluacion/', evaluationManager, name='gestionEvaluacion'),
	path('cancelarEv/<int:pk>/', CancelarEvaluacion.as_view(), name = 'cancelarEv'),
	path('modificarEv/<int:pk>/', ModificarEvaluacion.as_view(), name = 'modificarEv'),
	path('evaluacionPendiente/', EvaluacionesPendientes, name='evPendientes'),
	path('perfilEstudiante/<username>/', PerfilEstudiante, name = 'perfilE'),
	path('evaluarDocente/', evaluarDocente, name='evaluarDocente'),
	path('verNotas/', verNotas, name='verNotas'),
	]