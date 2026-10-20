from django.db import models
#Modelo de pagina definido
# Create your models here.
class Page(models.Model):#Heredamos de models
    #definimos los campos del modelo y aplicamos verbose_name para traducir los campos en el papel de administracion
    title = models.CharField(max_length=50, verbose_name= "Titulo")
    content = models.TextField(verbose_name= "Contenido")
    slug = models.CharField(unique=True, max_length=150, verbose_name= "URL amigable") #url que va atener la pagina
    #unique para que sea unico
    visible = models.BooleanField(verbose_name= "¿Visible?")
    #auto_now_add= True para que adicione la fecha de cuando se crea
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= "Creación:")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name= "Actualización:")

    class Meta:
        verbose_name= "Pagina"
        verbose_name_plural= "Paginas"
        #Metodo str para que cuando se muestre el objeto imprima un string
        def __str__(self):
            return self.title
        

