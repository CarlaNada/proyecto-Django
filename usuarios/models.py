from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(
        max_length=50, 
        null=True, 
        blank=True
    )
    """
    foto = models.ImageField(
        upload_to='users_foto/', 
        null=True, 
        blank=True
    )
    """
    def __str__(self):
        return f'{self.username}'
    
#DATOS DE PRUEBA
#User comun = carla99
#Password = admin.123

#User staff= mawli
#Password = crud1234