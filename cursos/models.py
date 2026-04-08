from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()
    precio = models.IntegerField()
    nivel = models.CharField(max_length=100)
    modalidad = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Soy el curso {self.nombre}'
