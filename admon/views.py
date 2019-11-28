from django.shortcuts import render, redirect
from .models import *
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from .models import *
from .forms import *
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




