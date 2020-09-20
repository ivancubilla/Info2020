from django.shortcuts import render
from .models import Ciudad,Publicacion
from .forms import PublicacionForm, PublicacionFilter
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
# Create your views here.

# class publicacionCrear(CreateView):
# 	model = Publicacion
# 	form_class = PublicacionForm
# 	template_name = 'crear_publicacion.html'
# 	success_url = reverse_lazy('index')

# class publicacionList(ListView):
# 	model = Publicacion
# 	queryset = Publicacion.objects.filter(ciudad = '002')
# 	template_name = 'index.html'

def crearPublicacion(request):
	if request.method == 'GET':
		form = PublicacionForm()
		contexto = {
			'form':form
		}
	else:
		form = PublicacionForm(request.POST)
		contexto = {
			'form':form
		}
		print(form)
		if form.is_valid():
			form.save()
			return redirect('index')
	return render(request, 'crear_publicacion.html', contexto)

def inicio(request):
	publicaciones = Publicacion.objects.all()
	filtro = PublicacionFilter(request.GET, queryset = publicaciones)
	contexto = {
		'filtro':filtro,
		} 
	return render(request, 'index.html',contexto)