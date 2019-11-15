from django.shortcuts import render, redirect
from .models import *
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
<<<<<<< HEAD
    	if filtro[0].get('tipo_usuario')=='m':
    		return redirect('admon:bienvenida')            
=======
    	if filtro[0].get('tipo_usuario')=='e':
    		return redirect('admon:listado_consulta')   #sustituir listado_consulta por el del estudiante        
>>>>>>> e332e4e2619bcfbb200279d997229e9f098ce8cd
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
