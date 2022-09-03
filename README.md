# djangoBlog
Proyecto final de la comisión CoderHouse Python 31095. Matías Moreno y Martín Prozapas. 
```

1) django-admin startproject Blog
2) cd Blog
3) python3 manage.py startapp Articulos
4) python3 manage.py runserver
5) python3 manage.py migrate
6) python3 manage.py makemigrations
********************************************************************************
Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) 
into your database schema. They're designed to be mostly automatic, but you'll need to know when to make migrations, 
when to run them, and the common problems you might run into.
********************************************************************************
6bis) Creo carpeta Blog/templates/bienvenida
********************************************************************************
7) views.py, def home(request):
	return render(request, 'bienvenida.html')

********************************************************************************
8) urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
********************************************************************************
9) settings.py, TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
********************************************************************************
10) models.py
Me permitirá tener todos los modelos y entradas y tenerlos en la BD como admin.
class Entrada(models.Model): ##clase con herencia
	nombre = models.CharField(max_length=50) #¿Qué es lo que quiero mostrar?

# Create your models here.
class Entrada(models.Model): 
    nombre = models.CharField(max_length=50)
    contenido = models.CharField(max_length=400)
    imagen =  models.URLField()
    autor = models.CharField(max_length=50)
********************************************************************************
11) ctrl + c para detener el runserver, python3 manage.py makemigrations para generar la tabla SQL correspondiente.
********************************************************************************
12) settings.py
 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Articulos',
]
******************************************************************************** 
13) python3 manage.py makemigrations
********************************************************************************
14) python3 manage.py migrate
********************************************************************************
15) creamos el usuario admin: 
python3 manage.py createsuperuser
Username: martin 
enter
password: 4268
********************************************************************************
16) python3 manage.py runserver
********************************************************************************
17) http://127.0.0.1:8000/admin/login/?next=/admin/ [accedo]




********************************************************************************
18) admin.py
from django.contrib import admin
from Articulos.models import Entrada

# Register your models here.
admin.site.register(Entrada)
********************************************************************************
19) [actualizar vista admin]
En la app Articulos tendremos una tabla a la que podremos acceder desde Entradas. 
********************************************************************************
20) entradas, click en Add. 
Muestra la tabla SQL con los campos Nombre, contenido, imagen, autor.
********************************************************************************
21) models.py
class Entrada(models.Model): 
    nombre = models.CharField(max_length=50)
    contenido = models.TextField(max_length=400) #ampliamos el campo de contenido 
    //ctrl c, makemigrations (busca los cambios), migrate (aplica los cambios), runserver
    imagen =  models.URLField()
    autor = models.CharField(max_length=50)
********************************************************************************
22) [admin] 
completo campos nombre, contenido, image (url de la img) y autor, click en guardar. 
********************************************************************************
23) Muestra entrada object. Para cambiar esta vista, 
models.py
def __str__(self):
        return self.nombre
********************************************************************************
24) views.py
from Articulos.models import Entrada
¿Cómo consultamos esos artículos que tenemos en la BD?

# Create your views here.
def home(request):
    articulos = Entrada.objects.all()
	return render(request, 'bienvenida.html', {'articulos':articulos}) //creamos un diccionario 
  que se llamará artículos (key) y que tendrá como valor la variable que acabamos de crear, artículos. 
	Le estamos diciendo que consulte todos los artículos y que los mande al template. 
********************************************************************************
Fuente: https://es.stackoverflow.com/questions/111253/cual-es-la-diferencia-entre-git-push-u-origin-master-y-git-push-origin-master
git push -u upstream master

La u significa upstream y se refiere al repositorio remoto principal al que harás pull y push, esta opción se utiliza una sola vez.

Cuando tienes mas de un repositorio remoto puedes utilizar esta opción para configurar uno de ellos como el principal... 
suponiendo que tienes un repo en BitBucket (bitbucket), otro en GitHub (origin) y otro en GitLab (gitlab) 
y quisieras utilizar GitHub (origin) como principal, tendrías que hacer git push -u origin <branch> 
y las siguientes veces al hacer solo git push lo hará a GitHub sin tener que especificar 
el repositorio pero para los otros dos si tendrías que hacerlo, ej. git push bitbucket <branch> 
o git push gitlab <branch>. Igual si tienes un solo repositorio y quieres evitar estar escribiendo 
git push origin <branch> puedes utilizar esta opción y solo hacer git push las siguientes veces.

A esta opción también se le conoce como "argument-less git-pull/push (git-pull/push sin argumentos)"
********************************************************************************
25) bienvenida.html
Ciclo for dentro del template, para ver los artículos.

<body>
    <h1>Bienvenidos a nuestro Blog</h1>
    <section>
        {% for elemento in articulos %}
            <article>
                <h3>{{ elemento.nombre }}</h3> 
            </article>
        {% endfor %}
 
    </section>
</body>

http://127.0.0.1:8000/

26) Estará mostrando
Django 1966
Django Unchained
¿De dónde viene esto?:
26.1 En models.py creé la clase:
class Entrada(models.Model): 
    nombre = models.CharField(max_length=50)
    contenido = models.TextField(max_length=400)
    imagen =  models.URLField()
    autor = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

26.2 En views.py creo la var articulos (render)
26.3 En el HTML:
        {% for elemento in articulos %}
            <article>
                <h3>{{ elemento.nombre }}</h3> 
            </article>
        {% endfor %}
 
27) Como no quiero que vean solamente el título, sino también el contenido del artículo, creo un <p>

28) Con esto vemos las imágenes:	

		<section>
			{% for elemento in articulos %}
			<article>
				<h3>{{ elemento.nombre }}</h3>
				<p>{{ elemento.contenido }}</p>
				<img src='{{ elemento.imagen }}' alt='' />
			</article>
			{% endfor %}
		</section>

29) agregamos un footer
30) Dentro de carpeta Articulos, creamos carpeta static. Dentro de esta última carpeta, estilos.css

31) estilos.css
Se aplicará a todos los elementos:
*{
    border: 0;
    box-sizing: border-box; 
    margin: 0;
    padding: 0;
} (...)

32) bienvenida.html, Para cargar el css
		{% load static %} <link rel='stylesheet' type='text/css' href='{% static
		'estilos.css' %}'>
```
