from django.shortcuts import  render, HttpResponse, redirect
from miapp.models import Article, Category

# Create your views here.
# MVC Modelo Vista Controlador -> Acciones (Metodos)
# MVT Modelo Template Vista -> Acciones (Metodos)

layout = """
<h1>Sitio Web con Django | ADSO SENA</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
        <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr/>       
"""

def index(request):

    html = """
            <h1>Inicio</h1>
            <p>Años hasta el 2050:</p>
            <ul>
    """
    year = 2026
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"

    nombre= 'Carlos Gomez'
    lenguajes = [ 'JavaScript', 'Python', 'PHP', 'C#', 'Java',  'C++']

    return render(request, 'index.html', {
        'title': "Inicio 2",
        'mi_variable': "Soy un dato que esta en la vista",
        'nombre': nombre,
        'lenguajes': lenguajes
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect("/inicio/")

    return render(request, 'pagina.html')

def contacto(request, nombre="", apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title=title,
        content=content,
        public=public
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulo(request):

    try:
        articulo = Article.objects.get(title= "Matrix", public=False) #objects=get(pk=1) #objects= es un metodo de django que permite traer un objeto de la base de datos, en este caso el articulo con id 1
        response = f"Articulo: <br/> {articulo.id} <strong>{articulo.title}</strong> - {articulo.content}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True
    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} actualizado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulos(request):

    articulos = Article.objects.all() # Trae todos los articulos de la base de datos

    #Consultas con condiciones filter para filtrar por un valor especifico
    articulos = Article.objects.filter(title__exact= "articulo") # Trae todos los articulos publicos de la base de datos

    articulos = Article.objects.filter(
                                title= "Articulo", 
                                ).exclude(
                                    public=True
                                ) # Trae todos los articulos que contengan la palabra articulo en el titulo y que no sean publicos
    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo' AND public=0") # Trae todos los articulos que contengan la palabra articulo en el titulo y que no sean publicos

    return render(request, 'articulos.html', {
        'articulos': articulos

    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')