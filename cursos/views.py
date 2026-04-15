from django.shortcuts import render
from .models import Curso

def inicio(request):
    return render(request, 'cursos/index.html')

def cursos(request):
    cursos = Curso.objects.all().order_by("-id")
    return render(request, 'cursos/cursos.html', {'cursos': cursos})