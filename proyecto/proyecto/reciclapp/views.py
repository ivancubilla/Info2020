from django.shortcuts import render
from django.http import HttpResponse
from .forms import PublicarForm

# Create your views here.


def index(request):
	return render(request, "index.html")


def Resistencia(request):
	return render(request, "Resistencia.html")


def Barranqueras(request):
	return HttpResponse(request, "Barranqueras.html")


def SaenzPena(request):
	return render(request, "SaenzPena.html")


def Publicar(request):
	context = {}
	context['form'] = PublicarForm()
	return render(request, "SaenzPena.html", context)
# 	#return HttpResponse(request, "Publicar.html")

# def Publicar(request):

# 	if request.method=="POST":
# 		miFormulario=PublicarForm(request.POST)

# 		if miFormulario.is_valid():
# 			infForm=miFormulario.cleaned_data

# 			return render(request, "Resistencia.html")

# 	else:
# 		miFormulario=PublicarForm()

# 	return render(request, "SaenzPena.html", {"form":miFormulario})