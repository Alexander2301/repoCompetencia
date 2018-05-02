from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Marca(models.Model):
	nombre= models.CharField(max_length= 50)

	def __str__(self):
		return self.nombre

class Bicicleta(models.Model):
	color = models.CharField(max_length= 50)
	serie= models.CharField(max_length= 20)
	marca = models.ForeignKey(Marca, on_delete= models.CASCADE)

	def __str__(self):
		return self.serie


class Competencia(models.Model):
	nombre= models.CharField(max_length= 50)

	def __str__(self):
		return self.nombre

class Categoria(models.Model):
	nombre= models.CharField(max_length= 50)

	def __str__(self):
		return self.nombre
		
class Nacionalidad(models.Model):
	nombre= models.CharField(max_length= 50)

	def __str__(self):
		return self.nombre

class Corredor(models.Model):
	nombre= models.CharField(max_length= 50)
	edad= models.IntegerField()
	categoria = models.ManyToManyField(Categoria, null= True, blank= True)
	nacionalidad =models.ForeignKey(Nacionalidad, on_delete= models.CASCADE)
	bicicleta = models.ManyToManyField(Bicicleta, null= True, blank= True)
	competencia = models.ManyToManyField(Competencia, null= True, blank= True)
	foto       =   models.ImageField(upload_to= 'fotos', null= True, blank= True)

	def __str__(self):
		return self.nombre

class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	foto = models.ImageField(upload_to= 'perfil', null=True, blank=True)
	nombre = models.CharField(max_length= 100)
