from django import forms
from django.core import validators

class FormArticle(forms.Form): #Hereda de la clase forms

    #creamos las propiedades
    title = forms.CharField(
        label= "Titulo",
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite el titulo',
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator(r'^[\w\s-]+$', 'El titulo esta mal formado', 'invalid_title')#expresion regular

        ]
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
         