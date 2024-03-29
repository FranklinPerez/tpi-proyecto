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

from django.db.models import Q

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


        if filtro[0].get('tipo_usuario')=='p':
            return redirect('admon:bienvenida')

        if filtro[0].get('tipo_usuario')=='e':
            return redirect('admon:perfilE', usuario)   #sustituir listado_consulta por el del estudiante        

        else:
            if filtro[0].get('tipo_usuario')=='d': 
                return redirect('admon:gestion_cita')  #sustituir gestion_cita por el del docente

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
    materia=Materia.objects.filter(profesor__usuario__codUsu=profesor).filter(codMat=materia).values('estudiantes')
    mat=Materia.objects.filter(codMat=materia)
    estudiantes=[]
    i=0
    for est in materia:
        est=Estudiante.objects.filter(nieEst=materia[i].get('estudiantes')).values('nieEst','nomEst')
        estudiantes.append(est)
        i=i+1
    

    return render(request,'plantillas/registroNotas.html',{'estudiantes':estudiantes})


def registrarNota(request, est,mat):


    return render(request,'plantillas/registroNotas.html')

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



































































































































###   CODIGO DE RUDDY   ===============================================


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
    evP = EvaluacionDocente.objects.filter(estado = 1).order_by('fecVen')
    evF = EvaluacionDocente.objects.filter(estado = 2)
    ev = EvaluacionDocente.objects.filter(estado = 1).filter(fecVen__lt = datetime.now())

    return render(request, 'plantillas/evaluationManager.html', {'evP':evP, 'evF':evF,'ev':ev})

class CancelarEvaluacion(DeleteView):
    template_name = 'plantillas/cancelarEvaluacion.html'
    model = EvaluacionDocente
    success_url = reverse_lazy('admon:gestionEvaluacion')

class ModificarEvaluacion(UpdateView):
    template_name = 'plantillas/modificarEvaluacion.html'
    form_class = ModificarEvaluacionForm
    model = EvaluacionDocente
    success_url = reverse_lazy('admon:gestionEvaluacion')

def estadoEvaluacion(request):
    e = EvaluacionDocente.objects.filter(estado = 1).filter(fecVen__lt = datetime.now()).update(estado = 2)
    return render(request, 'plantillas/estadoEvaluacion.html', {'e':e})
   

def EvaluacionesPendientes(request, pk):
    ev = EvaluacionDocente.objects.filter(estado = 1).order_by('numEva').filter(profes__actividad__notEst_id = pk).exclude(evaluacion__estudiante_id = pk).distinct()
    est = Estudiante.objects.get(pk = pk)
    
    return render(request, 'plantillas/evPendientes.html', {'ev':ev,'est':est})

# Vista del estudiante para evaluar al docente-------------------------------------
def evaluarDocente(request, pk, pk2):
    est = Estudiante.objects.get(nieEst = pk)
    ev = EvaluacionDocente.objects.filter(estado = 1).get(profes__codPro = pk2)

    if request.method == 'POST':
        form = EvaluacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admon:evPendientes', est.nieEst)
    else:
        form=EvaluacionForm()

    return render(request, 'plantillas/evaluarDocente.html', {'form':form, 'ev':ev, 'est':est})

def verNotas(request):
    pk = request.GET.get('action', None)

    e = Estudiante.objects.get(nieEst = pk)
    r = Actividad.objects.filter(notEst = pk).filter(year = datetime.now().year).order_by('notMat', 'periodo')
    m = Materia.objects.filter(actividad__notEst = pk).filter(actividad__year = datetime.now().year).distinct().order_by('codMat')

    return render(request, 'plantillas/verNotas.html',  {'e':e, 'r':r,'m':m})

def PerfilEstudiante(request, usuario):
    e = Estudiante.objects.get(usuario__codUsu = usuario)
    model = Estudiante
    form = PerfilEstudianteForm(request.POST, instance = e)

    return render(request, 'plantillas/perfilEstudiante.html', {'form':form, 'e':e} )

##### FINAL CODIGO DE RUDDY     =================================================================================



   

