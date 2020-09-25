from django import forms
from .models import Publicacion
import django_filters

class DateInput(forms.DateInput):
	input_type = 'date'

class PublicacionForm(forms.ModelForm):
	peso_aprox = forms.IntegerField(label='Peso Aproximado')
	class Meta:
		model = Publicacion
		fields = '__all__'
		widgets = {'fecha_fin' : DateInput()}

class PublicacionFilter(django_filters.FilterSet):
	class Meta:
		model = Publicacion
		fields = ['ciudad','tipo','fecha_fin']
		