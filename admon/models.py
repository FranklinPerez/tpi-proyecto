from django.db import models
from datetime import *
from django.utils import timezone

# Create your models here.
#modelo para los usuarios del sistema
class Usuario(models.Model):
	codUsu=models.CharField(max_length=10,help_text="Ingrese el Usuario, maximo 10 caracteres",primary_key = True)
	pasUsu=models.CharField(max_length=20,help_text="Ingrese contraseña, maximo 20 caracteres")

	TIPO_USUARIO= (
		('s','Profesor'),
		('m', 'Medico'),		
		)

	tipo_usuario= models.CharField(
        max_length=10,
        choices=TIPO_USUARIO,
        blank=True,
        default='sssssqqqqq',
        help_text='Tipo de usuario en el sistema')

	def __str__(self):
		 return '{0}, {1},{2}'.format(self.codUsu, self.pasUsu, self.tipo_usuario)
#fin modelo para los usuarios del sistema

# modelo para los estudiantes del sistema
class Estudiante(models.Model):
	nieEst=models.IntegerField(max_length=10,help_text="Codigo del MINED asignado al estudiante",primary_key=True)
	nomEst=models.CharField(max_length=20,help_text="Primer y/o segundo nombre del estudiante")
	apeEst=models.CharField(max_length=20,help_text="Primer y/o segundo apellido del estudiante")
	fecNac=models.DateField(null=False, blank=True)
	graEst=models.ForeignKey('Grado', on_delete=models.SET_NULL, null=True)
	nomPad=models.CharField(max_length=100,help_text="Nombre del padre")
	nomMad=models.CharField(max_length=100,help_text="Nombre de la madre")
	dirEst=models.CharField(max_length=100,help_text="Direccion del estudiante")
	def __str__(self):
		return self.nieEst
#fin modelo para los estudiantes del sistema

# modelo para los grados de educacion que cursan los estudiantes
class Grado(models.Model):
	nomGra=models.CharField(max_length=15,help_text="nombre del grado", primary_key=True)
	nivGra=models.CharField(max_length=20,help_text="nivel del grado (primer ciclo, segundo ciclo, etc)")
	seccion=models.CharField(max_length=1,help_text="Seccion del grado")
#fin modelo para los grados de educacion que cursan los estudiantes

# modelo para las materias que cursan los estudiantes
class Materia(models.Model):
	codMat=models.CharField(max_length=15,help_text="codigo de la materia", primary_key=True)
	nomMat=models.CharField(max_length=15,help_text="nombre de la materia")
	graMat=models.ForeignKey('Grado', on_delete=models.SET_NULL, null=True)
	proMat=models.ForeignKey('Profesor', on_delete=models.SET_NULL, null=False)
#fin modelo para los materias que cursan los estudiantes

# modelo para los profesores
class Profesor(models.Model):
	codPro=models.CharField(max_length=15,help_text="codigo del profesor", primary_key=True)
	nomPro=models.CharField(max_length=100,help_text="nombre del profesor")	
#fin modelo para los profesores