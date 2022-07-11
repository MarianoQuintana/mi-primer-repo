from django.contrib import admin
from django.urls import path
from mi_app.views import (saludar_a, saludo,
           saludo_personalizado, familia, curso, listar_estudiantes, mostrar_index)



urlpatterns = [
    path("mi-pagina/", mostrar_index),
    path("saludar/persona/<nombre>", saludar_a),
    path("saludo-personalizado/", saludo_personalizado),
    path("familia/", familia),
    path("lista_cursos/", curso),
    path("listar_estudiantes/", listar_estudiantes)
        ]