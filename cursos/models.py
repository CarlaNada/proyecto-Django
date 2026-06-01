from django.db import models

class Modalidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Modalidades"

class Nivel(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre   

    class Meta:
        verbose_name_plural = "Niveles"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()
    precio = models.IntegerField()    
    activo = models.BooleanField(default=True)
    modalidad = models.ForeignKey(
        Modalidad, 
        on_delete=models.CASCADE, 
        related_name="modalidad", 
        default=None, 
        null=True, 
        blank=True
    )
    nivel = models.ForeignKey(
        Nivel,
        on_delete=models.CASCADE,
        related_name="nivel",
        default=None, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return f'Curso de {self.nombre}'
    
    class Meta:
        verbose_name_plural = "Cursos disponible"
        ordering = ["-id"]
    
