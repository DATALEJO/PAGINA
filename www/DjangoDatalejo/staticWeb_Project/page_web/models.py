from django.db import models


# Create your models here.
class ListaNavbar(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=20)
    contenido = models.CharField(max_length=100)
    imagen = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo
