from django import forms
from .models import Curso

class CursoForm (forms.ModelsForm):
    class Meta:
        model = Curso
        fields = [
            "nombre", 
            "duracion", 
            "precio", 
            "modalidad", 
            "nivel",
        ]