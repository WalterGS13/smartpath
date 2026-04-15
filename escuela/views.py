from django.shortcuts import render
from escuela.models import *

def maestro(request):
    
    maestro_usuario = maestros.objects.filter(id_usuario = usuarios.objects.filter(id_usuario = 1)[0])[0]

    students = alumnos.objects.all()

    return render(request, "escuela/maestro.html", {"maestro": maestro_usuario, "alumnos": students})
