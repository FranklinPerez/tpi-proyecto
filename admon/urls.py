from .ajax import load_Docentes
from django.urls import path, include, re_path
from .views import *

app_name = 'admon'
urlpatterns=[
	path('index/', index, name='index'),

	path('iniciarSesion', iniciarSesion, name='inicarsesion'),
	path('autenticarUsuario', autenticarUsuario, name='autenticar_usuario'),
	path('cerrarSesion', cerrarSesion, name='cerrar_sesion'),
	path('bienvenida', bienvenida, name='bienvenida'),
	
	
    path('secretaria/',secretaria,name='secretaria'),
    path('vistaNotaMateria/<str:materia>+<str:profesor>/', vistaNotaMateria, name='vistaNotaMateria'),

    path('gestionProfesor/', ListadoProfesor.as_view(), name='listado_Profesor'),
    path('registrarProfesor/', crearProfesor.as_view(), name='crearProfesor'),
    path('modificarProfesor/<str:pk>/', ModificarProfesor.as_view(), name = 'modificarPro'),
	path('eliminarProfesor/<str:pk>/', EliminarProfesor.as_view(), name = 'eliminarPro'),

	path('gestionEstudiante/', ListadoEstudiante.as_view(), name='listado_Estudiante'),
    path('registrarEstudiante/', crearEstudiante.as_view(), name='crearEstudiante'),
    path('modificarEstudiante/<int:pk>/', ModificarEstudiante.as_view(), name = 'modificarEstudiante'),
	path('eliminarEstudiante/<int:pk>/', EliminarEstudiante.as_view(), name = 'eliminarEstudiante'),


	path('gestionMateria/', ListadoMateria.as_view(), name='listado_Materia'),
    path('registrarMateria/', crearMateria.as_view(), name='crearMateria'),
    path('modificarMateria/<int:pk>/', ModificarMateria.as_view(), name = 'modificarMateria'),
	path('eliminarMateria/<int:pk>/', EliminarMateria.as_view(), name = 'eliminarMateria'),


	path('gestionGrado/', ListadoGrado.as_view(), name='listado_Grado'),
    path('registrarGrado/', crearGrado.as_view(), name='crearGrado'),
    path('modificarGrado/<str:pk>/', ModificarGrado.as_view(), name = 'modificarGrado'),
	path('eliminarGrado/<str:pk>/', EliminarGrado.as_view(), name = 'eliminarGrado'),
















































	


	path('armarEvaluacion/', armarEvaluacion.as_view(), name='armarEvaluacion'),
	path('ajax/load_Docentes/', load_Docentes, name='load_Docentes'),
	path('evArmada', evArmada, name='armada'),
	path('gestionEvaluacion/', evaluationManager, name='gestionEvaluacion'),
	path('cancelarEv/<int:pk>/', CancelarEvaluacion.as_view(), name = 'cancelarEv'),
	path('estadoEvaluacion/', estadoEvaluacion, name = 'estadoEv'),
	path('modificarEv/<int:pk>/', ModificarEvaluacion.as_view(), name = 'modificarEv'),
	path('evaluacionPendiente/<pk>/', EvaluacionesPendientes, name='evPendientes'),
	path('perfilEstudiante/<username>/', PerfilEstudiante, name = 'perfilE'),
	path('evaluarDocente/<int:pk>/<int:pk2>/', evaluarDocente, name='evaluarDocente'),
	path('verNotas/', verNotas, name='verNotas'),

	]