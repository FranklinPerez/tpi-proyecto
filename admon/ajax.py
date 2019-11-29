from django.http import JsonResponse

from django.db.models import Q
from django.shortcuts import render
from .models import *


def load_Docentes(request):
	a = request.GET.get('pro')
	docentes = Profesor.objects.filter(estado = 'a').exclude(evaluaciondocente__estado__contains = 1)
	
	return render(request, 'hr/prof_dropdown_list.html', {'docentes': docentes})

