from django.contrib import admin

from aplicacion.appReciclapp.models import TipoDesecho
from aplicacion.appReciclapp.models import Publicacion
from aplicacion.appReciclapp.models import Localidad
from aplicacion.appReciclapp.models import Reciclable

# Register your models here.


class TipoDesechoAdmin(admin.ModelAdmin):
	search_fields = ("metal", "bombilladeluz", "escombros", "carton", "vidrio", "madera", "desechoselectronicos", "baterias")


class LocalidadAdmin(admin.ModelAdmin):
	search_fields = ("Resistencia", "Barranqueras", "P.R.Saenz Peña", "Charata", "Fontana", "Las Breñas", "Villa Angela", "Castelli")


class PublicacionAdmin(admin.ModelAdmin):
	search_fields = ("fecha", "hora")


admin.site.register(TipoDesecho, TipoDesechoAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Reciclable)
