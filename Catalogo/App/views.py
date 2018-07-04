from django.shortcuts import render
from .models import Noticia, Puntuacion

# Create your views here.
def mostrar_noticia(request):
    noticias = Noticia.objects.all()
    #puntuaciones = Puntuacion.objects.all()
    return render(request, 'noticias.html', {'todas_las_noticias':noticias})

def seccion_de_crear_noticias(request):
    return render(request, 'crear_noticias.html')

def guardar(request):
    a = request.POST['titulo']
    b = request.POST['fecha']
    c = request.POST['puntaje']

    nueva_noticia = Noticia(titulo=a, fecha=b, puntaje=c)
    nueva_noticia.save()

    return redirect('crear')

def puntuar(request, noticia_id):
    n = Noticia.objects.get(id=noticia_id)

    a = request.POST['cuerpo']
    
    nueva_puntuacion = Puntuacion(cuerpo=a, noticia=n)
    nueva_puntuacion.save()

    return redirect('noticias')