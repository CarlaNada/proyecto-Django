from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Curso
from .forms import CursoForm

def inicio(request):
    return render(request, 'cursos/index.html')

# READ
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/cursos.html', {'cursos': cursos})

# CREATE
## Requerido admin
@login_required
@permission_required('cursos.add_curso') #app.accion_modelo
def crearCurso(request):
    if request.method == 'POST':
        # logica agregar db
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
        else:
            print(form.errors)
    else:
        # logica mostrar form vacio
        form = CursoForm()

    return render(request, 'cursos/crear_curso.html', {"form" : form})

# UPDATE
## Requerido admin
@login_required
@permission_required('cursos.change_curso')
def editarCurso(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm(instance=curso)

    return render(request, 'cursos/editar_curso.html', {"form":form})

# DELETE
## Requerido admin
@login_required
@permission_required('cursos.delete_curso')
def borrarCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.activo = False
        curso.save()
        return redirect('cursos')

    return render(request, 'cursos/borrar_curso.html', {"curso":curso})
