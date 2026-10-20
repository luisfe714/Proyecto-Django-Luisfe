from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'layouts/mainapp/index.html',{
        'title': 'Inicio'
    })
#otra ruta
def about(request):
    return render(request, 'layouts/mainapp/about.html',{
        'title': 'Sobre Nosotros'
    })