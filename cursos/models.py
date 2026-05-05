from django.db import models
#from django.contrib.auth.model import User --> para acceder al modelo user de django

class Modalidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()
    precio = models.IntegerField()
    nivel = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, related_name="modalidad", default=None, null=True, blank=True)

    def __str__(self):
        return f'Soy el curso {self.nombre}'
