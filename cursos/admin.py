from django.contrib import admin
from .models import Curso, Modalidad, Nivel
# Register your models here.

admin.site.register(Modalidad)
admin.site.register(Nivel)

@admin.register(Curso)
class CursoAdmin (admin.ModelAdmin):
    list_display = ("id", "nombre", "duracion", "precio", "activo", "modalidad", "nivel",)
    list_filter = ("modalidad","nivel",)
    search_fields = ("nombre",)