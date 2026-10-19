from django.shortcuts import  render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import Q

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
        title=title, #title(nombre del modelo) = title(nombre de la variable)
        content=content,
        public=public
    )
    #Para guardar este articulo en la BD
    articulo.save()
    return HttpResponse(f"Articulo Creado: <strong>{articulo.title}</strong> - {articulo.content}")

#Copia de crear_articulo y lo llamamos save_articulo
def save_article(request):#No pasamos parametros por url y lo vamos a pasar por formulario
    if request.method == 'GET':
        title = request.GET['title']
        content = request.GET['content']
        public = request.GET['public']
        articulo = Article(
            title = title,
            content = content,
            public = public
        )
        #Para guardar este articulo en la BD
        articulo.save()
        return HttpResponse(f"Articulo creado: <strong> {articulo.title} - {articulo.content} </strong>")
    else:
        return HttpResponse(f"<h2> No se ha podido crear el articulo </h2>")

def create_article(request): #Soporte para plantilla para visualizar el formulario
    return render(request, 'create-article.html')

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

def articulos(request): #Creacion de la vista articulos
    #Creamos una template para listar varios articulos
    #1.Hacemos la peticion a la bd
    #Creamos la variable articulos y llamamos al modelo Article, usamos objects para poder hacer una consulta
    articulos = Article.objects.all().order_by('-id') #En este caso no usamos el metodo get si no el metodo all()
    #para sacar toda la informacion
    #dentro de articulos tenemos una lista de objetos un array de objetos
    """
    articulos = Article.objects.all() # Trae todos los articulos de la base de datos

    #Consultas con condiciones filter para filtrar por un valor especifico
    articulos = Article.objects.filter(title__exact= "articulo") # Trae todos los articulos publicos de la base de datos

    articulos = Article.objects.filter(
                                title= "Articulo", 
                                ).exclude(
                                    public=True
                                ) # Trae todos los articulos que contengan la palabra articulo en el titulo y que no sean publicos

    #Consultas con condiciones filter para filtrar por un valor especifico
    articulos = Article.objects.filter(title__contains = "Tiburon")

    #Realizar una consulta que muestre solo los que esten publicados y excluya bajo una condicion
    articulos = Article.onjects.filter (title = "Tiburon",).exclude(public = true)
    
    #Consulta ejecutando SQL
    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo' AND public=0") # Trae todos los articulos que contengan la palabra articulo en el titulo y que no sean publicos

    #Consulta utilizando el OR con ORM
    articulos = Article.objects.filter(
       Q(title__contains="Primer Articulo") | Q(title__contains="Batman")
    )
    """
    return render(request, 'articulos.html', { #pasamos el request y la template articulos.html y como tercer parametro
        'articulos': articulos  #Pasamos un diccionario con las variables que deseamos mostrar

    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')