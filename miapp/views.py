from django.shortcuts import render, HttpResponse,redirect

# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'Titulo': 'Inicio',
    })

def cursos(request):
    return render(request, 'cursos.html', {
        'Titulo': 'Cursos',
    })

def carreras(request):
    return render(request, 'carreras.html', {
        'Titulo': 'Carreras',
    })
def consultas(request):
    return render(request, 'consultas.html', {
        'Titulo': 'Consultas',
    })
def estudiantes(request):
    return render(request, 'estudiantes.html', {
        'Titulo': 'Estudiantes',
    })