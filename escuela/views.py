from django.shortcuts import render
from escuela.models import *
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

#redireccionando si ninguna clase fue seleccionada
def maestro(request):
    curso = cursos.objects.filter(id_maestro = maestros.objects.filter(id_usuario
    = usuarios.objects.filter(nombre_completo ="Andy Giancarlo Choreque Gomez")[0])[0])[0]    
    return HttpResponseRedirect(reverse("maestro_asistencia", args=(curso.nombre_curso,)))

def maestro_asistencia(request, n_curso):

    # obteniendo datos del curso filtrando por docente y su area
    curso = cursos.objects.filter(nombre_curso = n_curso, id_maestro = maestros.objects.filter(id_usuario
         = usuarios.objects.filter(nombre_completo ="Andy Giancarlo Choreque Gomez")[0])[0])[0]
        
    #obteniendo los estudiantes del grado en cuestion
   
    students = curso_asignado.objects.filter(id_curso = curso)

    #agregando automaticamente asistencia para cada alumno
    for student in students:
        if not asistencia.objects.filter(fecha = datetime.now(), id_alumno = student.id_alumno):
            attendance = asistencia(id_maestro = curso.id_maestro, id_alumno = student.id_alumno, estado = True)
            attendance.save()

    if request.method == "POST":
        # Cambio de asistencia
        alumno = alumnos.objects.filter(id_usuario = usuarios.objects.filter(nombre_completo = request.POST.get('q'))[0])[0]
        cambio_asistencia = asistencia.objects.filter(fecha= datetime.now(), id_alumno = alumno)[0]
        if cambio_asistencia.estado == True:
            cambio_asistencia.estado = False
        else:
            cambio_asistencia.estado = True

        cambio_asistencia.save()
       
        
        

    return render(request, "escuela/maestro.html", {"Curso": curso, "alumnos": students, "links": cursos.objects.filter(
        id_maestro = maestros.objects.filter(id_usuario
         = usuarios.objects.filter(nombre_completo ="Andy Giancarlo Choreque Gomez")[0])[0])})
