from django.db import models

# Create your models here.


class Publicacion(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    comentario = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.comentario


class Localidad(models.Model):
    tipo = [('0', ''), ('1', 'Resistencia'), ('2', 'Barranqueras'), ('3', 'P.R.Saenz Peña'), ('4', 'Charata'), ('5', 'Fontana'), ('6', 'Las Breñas'), ('7', 'Villa Angela'), ('8', 'Castelli')]
    tipos = models.CharField(max_length=1, choices=tipo, default='0')
    # contacto = models.ForeignKey()


class Reciclable(models.Model):
    unidad_medida = models.CharField(max_length=500)
    peso_aprox = models.IntegerField()


class TipoDesecho(models.Model):
    metal = models.BooleanField()
    bombilladeluz = models.BooleanField()
    escombros = models.BooleanField()
    carton = models.BooleanField()
    vidrio = models.BooleanField()
    madera = models.BooleanField()
    desechoselectronicos = models.BooleanField()
    baterias = models.BooleanField()
