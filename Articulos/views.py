from django.shortcuts import render
from Articulos.models import Entrada, Comentario

# Create your views here.
def home(request):
	articulos = Entrada.objects.all()
	if request.method == "POST":
		nombre = request.POST["nombre"]
		mensaje= request.POST["mensaje"]
		obj = Comentario(nombre=nombre,comentario=mensaje)
		obj.save()
		mensaje = "Gracias por tu opinion"
		return render(request,"bienvenida.html",{"articulos":articulos, "mensaje":mensaje})
	return render(request, 'bienvenida.html', {'articulos':articulos})