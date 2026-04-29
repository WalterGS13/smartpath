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
]
