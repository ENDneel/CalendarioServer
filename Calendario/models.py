from email.utils import format_datetime
from pyexpat import model
from django.db import models

# Create your models here.


class calendario(models.Model):
    fecha_i=models.DateTimeField(verbose_name="fecha_inicio")
    duracion=models.PositiveIntegerField(verbose_name="duracion")
    titulo=models.CharField(max_length=60,verbose_name="titulo")

    def __str__(self):
        return str(self.id)


class anuncio(models.Model):
    imagen=models.ImageField(upload_to='Anuncios')
    descripcion=models.CharField(verbose_name="descripcion", max_length=200)
    fecha_publicacion=models.DateField(verbose_name="fecha_publicacion")
    def __str__(self):
        return str(self.id)