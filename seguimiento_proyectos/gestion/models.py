from django.db import models
from django.contrib.auth.models import User  # Para asociar responsables a usuarios.

class Proyecto(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En Progreso', 'En Progreso'),
        ('Completado', 'Completado'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')

    def __str__(self):
        return self.nombre


class TareaProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='tareas', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_limite = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.proyecto.nombre})"
