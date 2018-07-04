from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=30)
    fecha = models.DateField()
    puntaje = models.CharField(max_length=30)

class Puntuacion(models.Model):
    cuerpo = models.CharField(max_length=50)
    noticia = models.ForeignKey(Noticia, related_name='puntuaciones', on_delete=models.CASCADE)