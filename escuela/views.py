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
        if not asistencia.objects.filter(fecha = datetime.now(), id_alumno = student.id_alumno, id_curso = student.id_curso):
            attendance = asistencia(id_maestro = curso.id_maestro, id_alumno = student.id_alumno, estado = True, grado_seccion = student.id_alumno.grado_seccion, id_curso = student.id_curso, fecha = datetime.now())
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

def asistencia_reporte(request):
    #cargando cursos 
    curso = cursos.objects.filter(id_maestro = maestros.objects.filter(id_usuario
    = usuarios.objects.filter(nombre_completo ="Andy Giancarlo Choreque Gomez")[0])[0])


    if request.method == "POST":
        curso_post = cursos.objects.filter(id_maestro = maestros.objects.filter(id_usuario
            = usuarios.objects.filter(nombre_completo ="Andy Giancarlo Choreque Gomez")[0])[0])[0]
        
    
        attendance = asistencia.objects.filter(id_maestro = curso_post.id_maestro, fecha = request.POST.get('date'), id_curso = cursos.objects.filter(nombre_curso = request.POST.get('curso'))[0])
      
        return render(request, "escuela/asistencia.html",{"cursos" : curso, "method": "post", "asistencias": attendance})
            
            
    return render(request, "escuela/asistencia.html",{"cursos" : curso, "method": "get", "asistencias": ""})

def asistencia_reporte_excepcion(request):
    if request.method == "POST":
        curso_excepcion = cursos.objects.filter(id_maestro = maestros.objects.filter(id_usuario
            = usuarios.objects.filter(nombre_completo ="Andy Giancarlo Choreque Gomez")[0])[0])[0]
        
    
        attendance_excusa = asistencia.objects.filter(id_maestro = curso_excepcion.id_maestro, fecha = request.POST.get('fecha'), id_curso = cursos.objects.filter(nombre_curso = request.POST.get('curso_asistencia'))[0], id_alumno =
                                                    alumnos.objects.filter(id_usuario = usuarios.objects.filter(nombre_completo = request.POST.get("nombre"))[0])[0])[0]
        
        attendance_excusa.excepcion = request.POST.get("excusa")
        attendance_excusa.save()
    
    return HttpResponseRedirect(reverse("asistencia"))


