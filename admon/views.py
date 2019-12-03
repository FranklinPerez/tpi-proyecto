from django.shortcuts import render, redirect
from django import forms
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from .models import *
from .forms import *
from datetime import *
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
# Create your views here.
def index(request):   

    return render(
        request,
        'base/base.html',
        context={},
    )
def iniciarSesion(request):   

    return render(
        request,
        'plantillas/login.html'
    )

def autenticarUsuario(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    filtro = Usuario.objects.filter(codUsu=username).filter(pasUsu=password).values('tipo_usuario')
    if filtro:

    	if filtro[0].get('tipo_usuario')=='p':
    		return redirect('admon:bienvenida')            

    	if filtro[0].get('tipo_usuario')=='e':
    		return redirect('admon:listado_consulta')   #sustituir listado_consulta por el del estudiante        

    	else:
    		if filtro[0].get('tipo_usuario')=='d': 
    		  return redirect('admon:gestion_cita')  #sustituir gestion_cita por el del docente
    else:
    	return render(request,'plantillas/errorUsuario.html')	

def cerrarSesion(request):
    return render(request,'plantillas/login.html')


def bienvenida(request):   

    return render(
        request,
        'base/base.html'
    )


class ListadoEstudiante(ListView):
    model = Estudiante
    template_name = 'plantillas/gestionEstudiante.html'
    context_object_name = 'estudiantes'
    
class crearEstudiante(CreateView):
    template_name = 'plantillas/crearEstudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('admon:listado_estudiante')

def VistaProfesor(request):
    return render(
        request,
        'plantillas/vistaProfesor.html'
    )

def VistaNota(request):
    estudiantes=Estudiante.objects.filter()
    return render(request, 'plantillas/vistaProfesor.html', {'evP':evP, 'evF':evF})


# Vista para que la Secre arme la evaluacion y quede activa de una-------------------
class armarEvaluacion(CreateView):
    template_name = 'plantillas/armarEvaluacion.html'
    form_class = ArmarEvaluacionForm
    success_url = reverse_lazy('admon:armada')

# Vista para confirmar la creacion de la evaluacion-------------------
def evArmada(request):
    return render(request, 'plantillas/evArmada.html')

# Vista para que la Secre borre o modifique la evaluacion-------------------
def evaluationManager(request):
    evP = EvaluacionDocente.objects.filter(estado = 1)
    evF = EvaluacionDocente.objects.filter(estado = 2)
    return render(request, 'plantillas/evaluationManager.html', {'evP':evP, 'evF':evF})

class CancelarEvaluacion(DeleteView):
    template_name = 'plantillas/cancelarEvaluacion.html'
    model = EvaluacionDocente
    success_url = reverse_lazy('admon:gestionEvaluacion')

class ModificarEvaluacion(UpdateView):
    template_name = 'plantillas/modificarEvaluacion.html'
    form_class = ModificarEvaluacionForm
    model = EvaluacionDocente
    success_url = reverse_lazy('admon:gestionEvaluacion')

# Vista del estudiante para evaluar al docente-------------------------------------
def evaluarDocente(request):
    e = EvaluacionDocente.objects.get(estado = 1)
    form = EvaluacionForm(request.POST)
    return render(request, 'plantillas/evaluarDocente.html', {'form':form, 'e':e} )

