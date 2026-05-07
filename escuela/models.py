from django.db import models

class roles(models.Model):
    nombre_rol = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_rol}"

class usuarios(models.Model):
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField()
    contrasena = models.CharField(max_length=128)
    rol = models.ForeignKey(roles, on_delete=models.CASCADE, related_name="rol")
    activo = models.BooleanField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre_completo
    

class padres_tutores(models.Model):
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="usuario_padre")
    telefono_emergencia = models.IntegerField()

class maestros(models.Model):
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="usuario_maestro")
    especialidad = models.CharField(max_length=100)
    def __str__(self):
        return self.id_usuario.nombre_completo
    
class grado(models.Model):
    grade = models.CharField(max_length=64)
    seccion = models.CharField(max_length=5)
    def __str__(self):
        return self.grade

class alumnos(models.Model):
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="usuario_alumno")
    grado_seccion = models.ForeignKey(grado, on_delete=models.CASCADE, related_name="grado")
    def __str__(self):
        return self.id_usuario.nombre_completo

class logs_auditoria(models.Model):
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="logs")
    evento = models.CharField(max_length=100)
    detalles = models.CharField(max_length=300)
    ip_address = models.GenericIPAddressField()
    created_at = models.DateField(auto_now=True)


class mensaje(models.Model):
    sender = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="mensaje_sender")
    receiver = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="mensaje_receiver")
    subject = models.CharField(max_length=50)
    message = models.CharField()
    date = models.DateTimeField(auto_now=True)

class relacion_familia(models.Model):
    id_padre = models.ForeignKey(padres_tutores,  on_delete=models.CASCADE, related_name="relacion_padre")
    id_alumno = models.ForeignKey(alumnos,  on_delete=models.CASCADE, related_name="relacion_alumnos")

class cursos(models.Model):
    nombre_curso = models.CharField(max_length=100)
    id_maestro = models.ForeignKey(maestros, on_delete=models.CASCADE, related_name="curso_maestro")
    curso_grado = models.ForeignKey(grado, on_delete=models.CASCADE, related_name="curso_grado")
    def __str__(self):
        return f"Curso: {self.nombre_curso} Maestro: {self.id_maestro.id_usuario.nombre_completo} Grado: {self.curso_grado.grade}"
    
class curso_asignado(models.Model):
    id_alumno = models.ForeignKey(alumnos,  on_delete=models.CASCADE, related_name="curso_alumno")
    id_curso = models.ForeignKey(cursos, on_delete=models.CASCADE, related_name="curso")

    def __str__(self):
        return self.id_alumno.id_usuario.nombre_completo +" de " + self.id_alumno.grado_seccion.grade + " en " + self.id_curso.nombre_curso
    


class pagos(models.Model):
    id_padre = models.ForeignKey(padres_tutores,  on_delete=models.CASCADE, related_name="pago_padre")
    monto = models.FloatField()
    fecha_pago = models.DateField()
    estado = models.BooleanField()

    def __str__(self):
        return f"{self.fecha_pago}"

class agenda_tareas(models.Model):
    id_curso = models.ForeignKey(cursos, on_delete=models.CASCADE, related_name="agenda_curso")
    grado_seccion = models.ForeignKey(grado, on_delete=models.CASCADE, related_name="agenda_grado")
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_entrega = models.DateField()
    nota = models.FloatField();

    def __str__(self):
        return f"Tarea: {self.titulo} Descripcion: {self.descripcion} Valor de la actividad: {self.nota}"
    
    
class asistencia(models.Model):
    id_maestro = models.ForeignKey(maestros, on_delete=models.CASCADE, related_name="asistencia_maestro")
    id_alumno = models.ForeignKey(alumnos,  on_delete=models.CASCADE, related_name="asistencia_alumnos")
    grado_seccion = models.ForeignKey(grado, on_delete=models.CASCADE, related_name="asistencia_grado")
    id_curso = models.ForeignKey(cursos, on_delete=models.CASCADE, related_name="asistencia_curso")
    fecha = models.DateField()
    excepcion = models.CharField(max_length=64)
    estado = models.BooleanField()
    def __str__(self):
        att = "Presente" if self.estado == True else "Ausente"
        ex = f"Motivo: {self.excepcion}" if self.excepcion != None else ""
        return f"Alumno {self.id_alumno.id_usuario.nombre_completo} estuvo {att} el dia {self.fecha} {ex}"

class calificaciones(models.Model):
    id_alumno = models.ForeignKey(alumnos,  on_delete=models.CASCADE, related_name="calificacion_alumnos")
    id_tarea = models.ForeignKey(agenda_tareas, on_delete=models.CASCADE, related_name="calificacion_tarea")
    id_curso = models.ForeignKey(cursos, on_delete=models.CASCADE, related_name="calificacion_curso")
    nota = models.FloatField()
    trimestre = models.IntegerField()
    def __str__(self):
        return f"Alumno: {self.id_alumno.id_usuario.nombre_completo} \n Tarea: {self.id_tarea.titulo}\n nota: {self.nota}"
    