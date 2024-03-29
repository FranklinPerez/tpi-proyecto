
from django import forms
from .models import *


class EstudianteForm(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields = {
			'nieEst','nomEst','apeEst','fecNac','dirEst','edadEst','ciudad',
		}
		labels = {
			'nieEst':'NIE del estudiante',
			'nomEst':'Nombre del estudiante',
		    'apeEst':'apellidodel estudiante',
		    'fecNac':'fecha de macimiento',
		    
		    'edadEst':'edad actual',
		    'dirEst':'Direccion',
		    'ciudad':'ciudad del estudiante',
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
		    'estado':'Estado',
		}


class MateriaForm(forms.ModelForm):
	class Meta:
		model = Materia
		fields = {
			'codMat','nomMat','profesor','estudiantes',
		}
		labels = {
			'codMat':'Codigo de la materia',
			'nomMat':'Nombre de la materia',
		    'profesor':'profesor de la materia',
		    'estudiantes':'estudiantes de la materia',
		}

class GradoForm(forms.ModelForm):
	class Meta:
		model = Grado
		fields = {
			'nomGra','nivGra', 'orientador', 'anio','materias',
		}
		labels = {
			'nomGra':'Codigo del profesor',
			'nivGra':'Nombre del profesor',
		    'orientador':'Estado',
		    'anio':'Estado',
		    'materias':'Estado',
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
		model = Evaluacion
		fields = {
			'evaluacion',
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
			'estudiante',
		}
		labels = {
			'evaluacion': '',
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
		    'totalE':'',
		    'estudiante':'',
		}
		widgets ={
			'evaluacion' : forms.TextInput(attrs={'type':'hidden'}),
			'totalE' : forms.TextInput(attrs={'type':'hidden'}),
			'estudiante' : forms.TextInput(attrs={'type':'hidden'}),
		}



class PerfilEstudianteForm(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields = {'nomEst', 'apeEst', }
		labels = {
			'nomEst':'',
			'apeEst':'',
			
		}	
