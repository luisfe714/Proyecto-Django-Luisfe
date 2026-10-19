from django import forms

class FormArticle(forms.Form): #Hereda de la clase forms

    #creamos las propiedades
    title = forms.CharField(
        label= "Titulo"
    )
    content = forms.CharField(
        label= "Contenido",
        widget=forms.Textarea
)
#Con choices se pueden pasar una serie de opciones
    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(#Permite mostrar un campo select y pasarle las opciones anteriores
        label = "¿Publicado?",
        choices = public_options
        )
         