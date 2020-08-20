from django.shortcuts import render, HttpResponse,redirect
from miapp.models import Curso
from django.db.models import Q

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
def crear_cursos(request):
    cursos = cursos(

    )
    cursos.save()
    return HttpResponse(f"cursos Creado: {cursos.titulo} - {cursos.contenido}")



def cursos(request):
    cursos = Curso.objects.all()          
    
    return render(request,"cursos.html",{
        'cursos': cursos,
        'titulo':'Listado de cursos'
    })

def eliminar_cursos(request, id):
    cursos = Curso.objects.get(pk=id)
    cursos.delete()
    return redirect('cursos')


def save_cursos(request):
    cursos = cursos(
        idcurso=idcurso,
        codigo=codigo,
        nombre=nombre,
        horas=horas,
        creditos=creditos,
        estado=estado
    )
    cursos.save()
    return HttpResponse(f"cursos Creado: {cursos.titulo} - {cursos.contenido}")



def crear_cursos(request, idcurso, codigo, nombre, horas, creditos, estado):
    curso = Curso(
        idcurso= idcurso,
        codigo = codigo,
        nombre = nombre,
        horas = horas,
        creditos = creditos,
        estado = estado        #titulo = titulo,
       # contenido = contenido,
        #publicado = publicado
    )
    curso.save()
    return HttpResponse(f"Curso Creado: {curso.nombre} - {curso.horas}")