from django.shortcuts import render
from escuela.models import *
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

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
    
    tareas = agenda_tareas.objects.filter(id_curso = curso)
    calificacion = calificaciones.objects.all()
    promedio = 0

    if tareas:
        for tarea in tareas:
            for c in calificacion:
                if c.id_tarea == tarea:
                    promedio = promedio + c.nota
            promedio = promedio/len(students)


        
       
    
    return render(request, "escuela/maestro.html", {"Curso": curso, "alumnos": students, "links": cursos.objects.filter(
        id_maestro = maestros.objects.filter(id_usuario
         = usuarios.objects.filter(nombre_completo ="Andy Giancarlo Choreque Gomez")[0])[0]), "promedio": promedio})

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

def maestro_tarea(request):
    if request.method == "POST":

        nueva_tarea = agenda_tareas(id_curso = cursos.objects.filter(nombre_curso = request.POST.get("nombre_curso"))[0],
                                    grado_seccion = grado.objects.filter(grade = request.POST.get("nombre_grado"))[0],
                                    titulo = request.POST.get("titulo"), descripcion = request.POST.get("descripcion"),
                                    fecha_entrega = request.POST.get("fecha_limite"), nota = request.POST.get("valor"))
        nueva_tarea.save()
    
    return HttpResponseRedirect(reverse("maestro_asistencia", args =(request.POST.get("nombre_curso"),)))

def tarea_calificacion(request):
    curso = cursos.objects.filter(id_maestro = maestros.objects.filter(id_usuario
    = usuarios.objects.filter(nombre_completo ="Andy Giancarlo Choreque Gomez")[0])[0])

    if request.method == "POST":
        curso_post = cursos.objects.filter(id = request.POST.get("curso"))[0]
        tarea = agenda_tareas.objects.filter(id_curso = curso_post, grado_seccion = curso_post.curso_grado)
        alumno = curso_asignado.objects.filter(id_curso = curso_post)
        return render(request, "escuela/calificacion_tareas.html", {"cursos" : curso, "tareas": tarea, "alumnos": alumno, "method":"post"})
     
    return render(request, "escuela/calificacion_tareas.html", {"cursos" : curso, "method": "get"})

def tarea_calificacion_nota(request):
    if request.method == "POST":
        calificacion = calificaciones(id_alumno = alumnos.objects.filter(id = request.POST.get("alumno"))[0], id_tarea = agenda_tareas.objects.filter(id = request.POST.get("tarea"))[0], nota = request.POST.get("nota"), trimestre = request.POST.get("trimestre"))
        calificacion.save()
    return HttpResponseRedirect(reverse("maestro"))


def message(request):
    
    user = usuarios.objects.filter(nombre_completo = "Andy Giancarlo Choreque Gomez")[0]
    mensajes = mensaje.objects.filter(sender = user).distinct("receiver").order_by("receiver","-date")
    
    
    return render(request, "escuela/mensajes.html",{"user": user, "mensajes": mensajes, "method": "get"})


def message_dm (request, name):
    user = usuarios.objects.filter(nombre_completo = "Andy Giancarlo Choreque Gomez")[0]
    mensajes = mensaje.objects.filter(sender = user, receiver = 
                                      usuarios.objects.filter(nombre_completo = name)[0]).order_by("date")
    
    m = mensaje.objects.filter(sender = usuarios.objects.filter(nombre_completo = name)[0], receiver = 
                                      user).order_by("date")

    mensajes = mensajes.union(mensajes, m)

    if request.method == "POST":
        new_message = mensaje(sender = user, receiver = usuarios.objects.filter(nombre_completo = name)[0], 
                              subject = request.POST.get("asunto"),
                              message = request.POST.get("message"))
        new_message.save()
        HttpResponseRedirect(reverse("message_dm", args=(name,)))
    

    
    return render(request, "escuela/mensaje_dm.html", {"user": user, "mensajes" : mensajes, "receiver": name})

def parent_student(request):
    usuario = relacion_familia.objects.filter(id_padre = padres_tutores.objects.filter(
            id_usuario = usuarios.objects.filter(nombre_completo = "John Smith")))


    

    




