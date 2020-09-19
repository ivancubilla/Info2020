from django.shortcuts import render
from .models import Ciudad,Publicacion
from .forms import PublicacionForm
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
# Create your views here.

class publicacionCrear(CreateView):
	model = Publicacion
	form_class = PublicacionForm
	template_name = 'crear_publicacion.html'
	success_url = reverse_lazy('index')

class publicacionList(ListView):
	model = Publicacion
	queryset = Publicacion.objects.filter(ciudad = '002')
	template_name = 'index.html'