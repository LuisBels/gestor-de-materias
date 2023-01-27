from django.shortcuts import render, redirect
from .models import Curso

# Create your views here.
def home(request):
  cursos = Curso.objects.all()
  return render(request, "gestionC.html",{
    "cursos":cursos
  })

def registroCurso(request):
  codigo = request.POST['txtCodigo']
  nombres = request.POST['txtNombre']
  creditos = request.POST['numCredito']

  curso = Curso.objects.create(codigo = codigo, nombre=nombres, creditos = creditos)

  return redirect('/')


def eliminacionCurso(request, codigo):
  curso = Curso.objects.get(codigo=codigo)
  curso.delete()

  return redirect('/')