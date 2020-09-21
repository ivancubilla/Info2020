from django import forms
from .models import Publicacion
import django_filters



class PublicacionForm(forms.ModelForm):
	class Meta:
		model = Publicacion
		fields = '__all__'


class PublicacionFilter(django_filters.FilterSet):
	class Meta:
		model = Publicacion
		fields = ['ciudad','tipo','fecha_fin']