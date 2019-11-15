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
    	if filtro[0].get('tipo_usuario')=='m':
    		return redirect('admon:bienvenida')            
    	else:
    		if filtro[0].get('tipo_usuario')=='s': 
    			return redirect('admon:gestion_cita')
    else:
    	return render(request,'plantillas/errorUsuario.html')	
def cerrarSesion(request):
    return render(request,'plantillas/login.html')


def bienvenida(request):   

    return render(
        request,
        'base/base.html'
    )
