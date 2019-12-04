from django.shortcuts import render, redirect
from django import forms
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from .models import *
from .forms import *
from datetime import *
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
import urllib
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
    
    usuario = request.POST.get('username')
    contrasena = request.POST.get('password')
    filtro = Usuario.objects.filter(codUsu=usuario).filter(pasUsu=contrasena).values('tipo_usuario')
    if filtro:
        if filtro[0].get('tipo_usuario')=='p':
            materias=Materia.objects.filter(profesor__usuario__codUsu=usuario)
            
            return render(request, 'plantillas/vistaProfesor.html',context = {'materias':materias, 'profesor':usuario})
        if filtro[0].get('tipo_usuario')=='s':
            return render(request,'plantillas/secretaria.html') 
    else:
        return render(request,'plantillas/errorUsuario.html')	

def cerrarSesion(request):
    return render(request,'plantillas/login.html')

class ListadoProfesor(ListView):
    model = Profesor
    template_name = 'plantillas/gestionProfesor.html'
    context_object_name = 'profesores'

class crearProfesor(CreateView):
    template_name = 'plantillas/crearProfesor.html'
    form_class = ProfesorForm
    success_url = reverse_lazy('admon:listado_Profesor')

def vistaNotaMateria(request, materia, profesor):
    materias=Materia.objects.filter(profesor__usuario__codUsu=profesor).filter(codMat=materia).values('estudiantes')
    mat=Materia.objects.filter(codMat=materia)
    estudiantes=[]
    i=0
    for est in materias:
        est=Estudiante.objects.filter(nieEst=materias[i].get('estudiantes'))
        estudiantes.append(est)
        i=i+1

    print(mat)
    return render(request,'plantillas/registroNotas.html',context = {'estudiantes':estudiantes})


def bienvenida(request):
    return render(request, 'base/base.html')

def secretaria(request):
    return render(request,'plantillas/secretaria.html')

class crearEstudiante(CreateView):
    template_name = 'plantillas/crearEstudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('admon:listado_Estudiante')

class ListadoEstudiante(ListView):
    model = Estudiante
    template_name = 'plantillas/gestionEstudiante.html'
    context_object_name = 'estudiantes'


class ModificarEstudiante(UpdateView):
    template_name = 'plantillas/modificarEstudiante.html'
    form_class = EstudianteForm
    model = Estudiante
    success_url = reverse_lazy('admon:listado_Estudiantes')

class EliminarEstudiante(DeleteView):
    template_name = 'plantillas/eliminarEstudiante.html'
    model = Estudiante
    success_url = reverse_lazy('admon:listado_Estudiantes')



class crearMateria(CreateView):
    template_name = 'plantillas/crearMateria.html'
    form_class = MateriaForm
    success_url = reverse_lazy('admon:listado_Materia')

class ListadoMateria(ListView):
    model = Materia
    template_name = 'plantillas/gestionMateria.html'
    context_object_name = 'materias'

class ModificarMateria(UpdateView):
    template_name = 'plantillas/modificarMateria.html'
    form_class = MateriaForm
    model = Materia
    success_url = reverse_lazy('admon:listado_Materia')

class EliminarMateria(DeleteView):
    template_name = 'plantillas/eliminarMateria.html'
    model = Materia
    success_url = reverse_lazy('admon:listado_Materia')


class ModificarProfesor(UpdateView):
    template_name = 'plantillas/modificarPro.html'
    form_class = ProfesorForm
    model = Profesor
    success_url = reverse_lazy('admon:listado_Profesor')

class EliminarProfesor(DeleteView):
    template_name = 'plantillas/eliminarProfesor.html'
    model = Profesor
    success_url = reverse_lazy('admon:listado_Profesor') 


class crearGrado(CreateView):
    template_name = 'plantillas/crearGrado.html'
    form_class = GradoForm
    success_url = reverse_lazy('admon:listado_Grado')

class ListadoGrado(ListView):
    model = Grado
    template_name = 'plantillas/gestionGrado.html'
    context_object_name = 'grados'

class ModificarGrado(UpdateView):
    template_name = 'plantillas/modificarGrado.html'
    form_class = GradoForm
    model = Grado
    success_url = reverse_lazy('admon:listado_Grado')

class EliminarGrado(DeleteView):
    template_name = 'plantillas/eliminarGrado.html'
    model = Grado
    success_url = reverse_lazy('admon:listado_Grado')






































































































































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




   

