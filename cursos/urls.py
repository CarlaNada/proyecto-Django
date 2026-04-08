from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('cursos/', views.cursos, name='cursos')
]
