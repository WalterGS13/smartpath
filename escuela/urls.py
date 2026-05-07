from django.urls import path
from escuela import views

urlpatterns = [
    path('maestro/', views.maestro, name= "maestro"),
    path('maestro/panel/<str:n_curso>', views.maestro_asistencia, name="maestro_asistencia"),  
    path('maestro/asistencia', views.asistencia_reporte, name="asistencia"),  
    path('maestro/asistencia/excepcion', views.asistencia_reporte_excepcion, name="asistencia_reporte_excepcion"),
    path('maestro/tarea', views.maestro_tarea, name = "maestro_tarea"),
    path('maestro/tarea/calificacion', views.tarea_calificacion , name = "tarea_calificacion"),
    path('maestro/tarea/calificacion/nota', views.tarea_calificacion_nota , name = "tarea_calificacion_nota"),
    path('mensajes/', views.message, name = "message"),
    path('mensajes/dm/<str:name>', views.message_dm, name = "message_dm"),
    path('padres_tutores/<str:name_parent>', views.pm_relative_member, name="padres_tutores"),
    path('alumno/<str:parent>/<str:name>', views.estudiante, name="estudiante"),
    path('padres_tutores/<str:name>/pago', views.metodo_pago, name="padres_tutores_pago"),
    
]
