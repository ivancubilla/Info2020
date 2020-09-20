from django.db import models

# Create your models here.

class Ciudad(models.Model):
	codigo = models.IntegerField(primary_key = True,null = False,blank = False,unique = True)
	nombre = models.CharField(max_length = 50)

	def __str__(self):
		txt = '{0}'
		return txt.format(self.nombre)

class Publicacion(models.Model):
	imagen = models.ImageField(blank = True, null = True,default='/publicaciones/default.png')
	codigo = models.AutoField(primary_key = True)
	fecha_post = models.DateTimeField()
	fecha_fin = models.DateField()
	desecho = [
			('0',''),
			('1','Carton'),
			('2','Vidrio'),
			('3','Madera'),
			('4','Escombros'),
			('5','Metal'),
			('6','Baterias'),
			('7','Desechos Electronicos'),
			('8','Bombillas de Luz')
			]
	tipo = models.CharField(max_length = 1, choices = desecho , default = '0')
	peso_aprox = models.SmallIntegerField(null = False, blank = False, default = '0')
	unidades = [
			('0',''),
			('1','g'),
			('2','Kg'),
			('3','Tn'),
			]
	unidad = models.CharField(max_length = 1, choices = unidades, default = '0')
	ciudad = models.ForeignKey(Ciudad,null = False,blank = False, on_delete = models.CASCADE)
	nombre = models.CharField(max_length = 50)
	apellido = models.CharField(max_length = 50)
	telefono = models.IntegerField()