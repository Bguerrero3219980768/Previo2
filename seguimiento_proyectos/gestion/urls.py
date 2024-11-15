from django.urls import path
from . import views

urlpatterns = [
    # Proyectos
    path('', views.lista_proyectos, name='lista_proyectos'),
    path('proyecto/<int:pk>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('proyecto/nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('proyecto/<int:pk>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('proyecto/<int:pk>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),

    # Tareas
    path('tarea/nueva/', views.crear_tarea, name='crear_tarea'),
]
