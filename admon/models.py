from django.db import models
from datetime import *
from django.utils import timezone
from .validators import solo_Letras, solo_Numeros, fecha_Mayor_Que_Hoy
from django.core.exceptions import ValidationError

# Create your models here.
#modelo para los usuarios del sistema
class Usuario(models.Model):
	codUsu=models.CharField(max_length=10,help_text="Ingrese el Usuario, maximo 10 caracteres",primary_key = True)
	pasUsu=models.CharField(max_length=20,help_text="Ingrese contraseña, maximo 20 caracteres")

	TIPO_USUARIO= (

		('p','Profesor'),
		('s', 'Secretaria'),		

		('e','Estudiante'),
		
		('o', 'Orientador'),		

		)

	tipo_usuario= models.CharField(
        max_length=10,
        choices=TIPO_USUARIO,
        blank=True,
        default='Estudiante',
        help_text='Tipo de usuario en el sistema')

	def __str__(self):
		 return '{0}, {1},{2}'.format(self.codUsu, self.pasUsu, self.tipo_usuario)
#fin modelo para los usuarios del sistema

# modelo para los estudiantes del sistema
class Estudiante(models.Model):
	nieEst=models.IntegerField(help_text="Codigo del MINED asignado al estudiante",primary_key=True)
	nomEst=models.CharField(max_length=20,help_text="Primer y/o segundo nombre del estudiante")
	apeEst=models.CharField(max_length=20,help_text="Primer y/o segundo apellido del estudiante")
	fecNac=models.DateField(null=False, blank=True)
	graEst=models.ForeignKey('Grado', on_delete=models.SET_NULL, null=True)	
	dirEst=models.CharField(max_length=100,help_text="Direccion del estudiante")
	edadEst=models.IntegerField(help_text="Edad actual del estudiante", null=True, blank=True)
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return self.nieEst
#fin modelo para los estudiantes del sistema

#modelo para el padre
class Padre(models.Model):
	duiPad=models.CharField(max_length=10, help_text="Codigo del padre", primary_key=True)
	nomPad=models.CharField(max_length=100,help_text="Nombre del padre")
	dirPad=models.CharField(max_length=100,help_text="Direccion del padre")
#fin modelo para el padre

#modelo para la madre
class Madre(models.Model):
	duiMad=models.CharField(max_length=10, help_text="Codigo de la madre", primary_key=True)
	nomMad=models.CharField(max_length=100,help_text="Nombre de la madre")
	dirMad=models.CharField(max_length=100,help_text="Direccion de la madre")
#fin modelo para la madre

#modelo para el representante
class Representante(models.Model):
	duiRep=models.CharField(max_length=10, help_text="Codigo del padre", primary_key=True)
	nomRep=models.CharField(max_length=100,help_text="Nombre del padre")
	dirRep=models.CharField(max_length=100,help_text="Direccion del representante")
#fin modelo para el representante

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
#fin modelo para los materias que cursan los estudiantes

# modelo para los profesores
class Profesor(models.Model):

	codPro=models.CharField(max_length=15,help_text="codigo del profesor", primary_key=True)
	nomPro=models.CharField(max_length=100,help_text="nombre del profesor")	
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)

	codPro=models.CharField(max_length=15,help_text="", primary_key=True)
	nomPro=models.CharField(max_length=100,help_text="",validators=[solo_Letras])	
	

	ESTADO= (

		('a','activo'),
		('i', 'inactivo'),			

		)

	estado= models.CharField(
        max_length=10,
        choices=ESTADO,
        blank=True,
        default='a',
        help_text='')

	def __str__(self):
		return self.nomPro
#fin modelo para los profesores

# modelo para registro de nota
class Actividad(models.Model):
	numReg=models.IntegerField(help_text="numero de registro", primary_key=True)
	nota=models.DecimalField(max_digits = 4, decimal_places = 2,help_text="nota del estudiante")	
	notMat=models.ForeignKey('Materia', on_delete=models.SET_NULL, null=True)
	notEst=models.ForeignKey('Estudiante', on_delete=models.SET_NULL, null=True)
	notPro=models.ForeignKey('Profesor', on_delete=models.SET_NULL, null=True)
	mes=models.ForeignKey('Mes', on_delete=models.SET_NULL, null=True)

	TIPO_NOTA= (

		('n','normal'),
		('r', 'reposicion'),			

		)

	tipo_nota= models.CharField(
        max_length=10,
        choices=TIPO_NOTA,
        blank=True,
        default='normal',
        help_text='Tipo de notadel estudiante')

#fin modelo para registro de nota

#modelo para departamento
class Departamento(models.Model):
	numDep = models.IntegerField(primary_key = True) 
	nomDep = models.CharField(max_length = 100, help_text = "Ingrese un departamento")
	def __str__(self):
		return self.nomDep
#fin modelo para departamento

#modelo para municipio
class Municipio(models.Model):
	numMunicipio = models.IntegerField(primary_key = True)
	nomMunicipio = models.CharField(max_length = 100, help_text = "Ingrese un municipio")
	departamento = models.ForeignKey('Departamento', on_delete = models.CASCADE)
	def __str__(self):
		return self.nomMunicipio	
#fin modelo para municipio

class Mes(models.Model):
	nomMes=models.CharField(max_length=15,primary_key=True)
	anio=models.CharField(max_length=4, help_text="año del Mes")

class Secretaria(models.Model):
	codSec=models.CharField(max_length=15,help_text="codigo del profesor", primary_key=True)
	nomSec=models.CharField(max_length=100,help_text="nombre del profesor")	
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)

























































































































































































# Modelo para la Evaluacion de Profesores
class EvaluacionDocente(models.Model):
	numEva = models.AutoField(primary_key=True)
	fecVen = models.DateField(null=False, blank=False, validators = [fecha_Mayor_Que_Hoy])
	profes = models.ForeignKey('Profesor', on_delete = models.PROTECT, null=False)

	VALOR_PREGUNTA = ((1,'Necesita Mejorar'), (2, 'Regular'),(3,'Bueno'), (4, 'Muy Bueno'),(5, 'Excelente'),)

	valPreg0 = models.IntegerField(choices = VALOR_PREGUNTA, null=True, blank = True)
	valPreg1 = models.IntegerField(choices = VALOR_PREGUNTA, null=True, blank = True)
	valPreg2 = models.IntegerField(choices = VALOR_PREGUNTA, null=True, blank = True)
	valPreg3 = models.IntegerField(choices = VALOR_PREGUNTA, null=True, blank = True)
	valPreg4 = models.IntegerField(choices = VALOR_PREGUNTA, null=True, blank = True)
	valPreg5 = models.IntegerField(choices = VALOR_PREGUNTA, null=True, blank = True)
	valPreg6 = models.IntegerField(choices = VALOR_PREGUNTA, null=True, blank = True)
	valPreg7 = models.IntegerField(choices = VALOR_PREGUNTA, null=True, blank = True)
	valPreg8 = models.IntegerField(choices = VALOR_PREGUNTA, null=True, blank = True)
	valPreg9 = models.IntegerField(choices = VALOR_PREGUNTA, null=True, blank = True)

	totalE = models.IntegerField( null=True, blank = True)

	ESTADO= ((1,'Pendiente'),(2, 'Finalizada'),)
	estado= models.IntegerField( choices=ESTADO, blank=True, default=1)

# Fin Modelo EvaluacionDocente
>>>>>>> 19a68492a6cec28be77738b38b5fe1df252015ea
