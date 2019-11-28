from django.http import JsonResponse

from django.db.models import Q
from django.shortcuts import render
from .models import *

from datetime import datetime, date

from django.core.exceptions import ValidationError

def solo_Letras(value):
	
	letras = " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóú";

	for i in value:
		if i not in letras:
			raise ValidationError('Solo se permiten letras')


def solo_Numeros(num):

	numeros = "0123456789";

	for i in num:
		if i not in numeros:
			raise ValidationError('Solo se permiten numeros enteros positivos')


def fecha_Mayor_Que_Hoy(f):
	hoy = datetime.now().date()
	if f < hoy:
		raise ValidationError('La fecha limite debe ser una fecha futura')
