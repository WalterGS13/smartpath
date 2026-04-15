from django.urls import path
from escuela import views

urlpatterns = [
    path('', views.maestro, name="maestro"),   
]
