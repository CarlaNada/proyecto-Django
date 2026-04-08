from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'cursos/index.html')

def cursos(request):
    return render(request, 'cursos/cursos.html')