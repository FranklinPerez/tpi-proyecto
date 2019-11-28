
from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget

class EstudianteForm(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields = {
			'nieEst','nomEst', 'apeEst','fecNac','graEst','dirEst','edadEst',
		}
		labels = {
			'nieEst':'NIE del estudiante',
			'nomEst':'Nombre del estudiante',
		    'apeEst':'apellidodel estudiante',
		    'fecNac':'fecha de macimiento',
		    'graEst':'grado a estudiar',
		    'edadEst':'edad actual',
		    'dirEst':'Direccion',
		}	
		
class ProfesorForm(forms.ModelForm):
	class Meta:
		model = Profesor
		fields = {
			'codPro','nomPro', 'estado',
		}
		labels = {
			'codPro':'Codigo del profesor',
			'nomPro':'Nombre del profesor',
		    'estado':'estado',
		}