from django.urls import path
from escuela import views

urlpatterns = [
    path('maestro/', views.maestro, name= "maestro"),
    path('maestro/panel/<str:n_curso>', views.maestro_asistencia, name="maestro_asistencia"),  
    path('maestro/asistencia', views.asistencia_reporte, name="asistencia"),  
]
