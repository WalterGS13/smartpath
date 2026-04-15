from django.db import models

class roles(models.Model):
    nombre_rol = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=100)

class usuarios(models.Model):
    id_usuario = models.IntegerField(auto_created=True, primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField()
    contrasena = models.CharField(max_length=128)
    rol = models.ForeignKey(roles, on_delete=models.CASCADE, related_name="rol")
    activo = models.BooleanField()
    created_at = models.DateField(auto_created=True)
    

class padres_tutores(models.Model):
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="usuario_padre")
    telefono_emergencia = models.IntegerField()

class maestros(models.Model):
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="usuario_maestro")
    especialidad = models.CharField(max_length=100)

class grado(models.Model):
    grade = models.CharField(max_length=64)
    seccion = models.CharField(max_length=5)

class alumnos(models.Model):
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="usuario_alumno")
    grado_seccion = models.ForeignKey(grado, on_delete=models.CASCADE, related_name="grado")

class logs_auditoria(models.Model):
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="logs")
    evento = models.CharField(max_length=100)
    detalles = models.CharField(max_length=300)
    ip_address = models.GenericIPAddressField()
    created_at = models.DateField(auto_now=True)

class relacion_familia(models.Model):
    id_padre = models.ForeignKey(padres_tutores,  on_delete=models.CASCADE, related_name="relacion_padre")
    id_alumno = models.ForeignKey(alumnos,  on_delete=models.CASCADE, related_name="relacion_alumnos")

class cursos(models.Model):
    nombre_curso = models.CharField(max_length=100)
    id_maestro = models.ForeignKey(maestros, on_delete=models.CASCADE, related_name="curso_maestro")

class pagos(models.Model):
    id_padre = models.ForeignKey(padres_tutores,  on_delete=models.CASCADE, related_name="pago_padre")
    monto = models.FloatField()
    fecha_pago = models.DateField(auto_now=True)
    estado = models.BooleanField()

class agenda_tareas(models.Model):
    id_curso = models.ForeignKey(cursos, on_delete=models.CASCADE, related_name="agenda_curso")
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_entrega = models.DateField()

class asistencia(models.Model):
    id_maestro = models.ForeignKey(maestros, on_delete=models.CASCADE, related_name="asistencia_maestro")
    id_alumno = models.ForeignKey(alumnos,  on_delete=models.CASCADE, related_name="asistencia_alumnos")
    fecha = models.DateField(auto_now=True)
    estado = models.BooleanField()

class calificaciones(models.Model):
    id_alumno = models.ForeignKey(alumnos,  on_delete=models.CASCADE, related_name="calificacion_alumnos")
    id_tarea = models.ForeignKey(agenda_tareas, on_delete=models.CASCADE, related_name="calificacion_tarea")
    nota = models.FloatField()
    trimestre = models.IntegerField()
    