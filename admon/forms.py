
from django import forms
from .models import *


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














































































































































































class ArmarEvaluacionForm(forms.ModelForm):
	class Meta:
		model = EvaluacionDocente
		fields = {'fecVen', 'profes', }
		labels = {
			'fecVen':'Fecha Limite ',
			'profes':'Docente a Evaluar ',
		}
		widgets ={
			'fecVen' : forms.DateInput(attrs={'class':'datepicker'}),
		}
			
class ModificarEvaluacionForm(forms.ModelForm):
	class Meta:
		model = EvaluacionDocente
		fields = {'fecVen', }
		labels = {
			'fecVen':'Fecha Limite ',
		}
		widgets ={
			'fecVen' : forms.DateInput(attrs={'class':'datepicker'}),
		}

class EvaluacionForm(forms.ModelForm):
	class Meta:
		model = EvaluacionDocente
		fields = {
			'valPreg0', 
			'valPreg1',
			'valPreg2',
			'valPreg3',
			'valPreg4',
			'valPreg5',
			'valPreg6',
			'valPreg7',
			'valPreg8',
			'valPreg9',
			'totalE',
		}
		labels = {
			'valPreg0':'',
		    'valPreg1':'',
		    'valPreg2':'',
		    'valPreg3':'',
		    'valPreg4':'',
		    'valPreg5':'',
		    'valPreg6':'',
		    'valPreg7':'',
		    'valPreg8':'',
		    'valPreg9':'',
		    'totalE':''
		}
		widgets ={
			'totalE' : forms.TextInput(attrs={'type':'hidden'}),
		}



class PerfilEstudianteForm(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields = {'nomEst', 'apeEst', 'graEst'}
		labels = {
			'nomEst':'',
			'apeEst':'',
			'graEst':'',
		}