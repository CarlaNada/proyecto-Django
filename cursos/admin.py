from django.contrib import admin
from .models import Curso, Modalidad, Nivel
# Register your models here.

# Una vista de administrador con al menos un filtro/búsqueda para alguno de los dos modelos (usar decorador @admin.register(Modelo))

admin.site.register(Curso)
admin.site.register(Modalidad)
admin.site.register(Nivel)