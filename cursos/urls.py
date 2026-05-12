from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('cursos/', views.cursos, name='cursos'),
    path('nueva/', views.crearCurso, name='crearCurso'),
    path('editar/<int:id>/', views.editarCurso, name='editarCurso'),
    path('borrar/<int:id>', views.borrarCurso, name='borrarCurso'),
]
