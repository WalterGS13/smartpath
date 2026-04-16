from django.shortcuts import render
from escuela.models import *
from datetime import datetime

def maestro(request):
    
    # obteniendo datos del curso filtrando por docente y su area
    curso = cursos.objects.filter(nombre_curso ="Ingles", id_maestro = maestros.objects.filter(id_usuario
        = usuarios.objects.filter(nombre_completo ="Andy Giancarlo Choreque Gomez")[0])[0])[0]

    #obteniendo los estudiantes del grado en cuestion
    students = alumnos.objects.filter(grado_seccion = curso.curso_grado.id)

    #agregando automaticamente asistencia para cada alumno
    for student in students:
        if not asistencia.objects.filter(fecha = datetime.now(), id_alumno = student):
            attendance = asistencia(id_maestro = curso.id_maestro, id_alumno = student, estado = True)
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
       
        
        

    return render(request, "escuela/maestro.html", {"Curso": curso, "alumnos": students})
