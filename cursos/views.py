from django.shortcuts import render
from .models import Curso
from .forms import CursoForm

def inicio(request):
    return render(request, 'cursos/index.html')

# READ
def cursos(request):
    cursos = Curso.objects.all().order_by("id")
    return render(request, 'cursos/cursos.html', {'cursos': cursos})

# CREATE
def crearCurso(request):
    if request.method == "POST":
        # logica agregar db
        pass
    else:
        # logica mostrar form vacio
        form = CursoForm()

    return render(request, 'TEMPLATE', {"form" : form})

# UPDATE

# DELETE