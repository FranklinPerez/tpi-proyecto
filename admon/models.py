from django.db import models

# Create your models here.
#modelo para los usuarios del sistema
class Usuario(models.Model):
	codUsu=models.CharField(max_length=10,help_text="Ingrese el Usuario, maximo 10 caracteres",primary_key = True)
	pasUsu=models.CharField(max_length=20,help_text="Ingrese contraseña, maximo 20 caracteres")

	TIPO_USUARIO= (
		('s','Secretaria'),
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

