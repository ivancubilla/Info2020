from django.shortcuts import render, redirect
from .models import Ciudad,Publicacion
from .forms import PublicacionForm, PublicacionFilter
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
from datetime import date
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
		form = PublicacionForm(request.POST, request.FILES)
		contexto = {
			'form':form
		}
		print(form)
		if form.is_valid():
			form.save()
			return redirect('index')
	return render(request, 'crear_publicacion.html', contexto)

def inicio(request):
	"""  Oculta pero la instancia sigue en la base de datos  """
#	hoy = date.today()
#	publicaciones = Publicacion.objects.filter(fecha_fin__gte=hoy).order_by('-fecha_post')
	"""  Se borra la instancia de la base de datos  """
	actualizar = Publicacion.objects.filter(fecha_fin__lt = date.today()).delete()
	publicaciones = Publicacion.objects.all().order_by('-fecha_post')
	filtro = PublicacionFilter(request.GET, queryset = publicaciones)
	contexto = {
		'filtro':filtro,
		} 
	return render(request, 'index.html',contexto)

def verPublicacion(request,id):
	try:
		p = Publicacion.objects.get(id = id)
	except Publicacion.DoesNotExist:
		raise Http404('No existe esa Publicacion')
	return render(request, 'publicaciones.html',{ 'p':p })

