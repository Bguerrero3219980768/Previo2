from django import forms
from .models import Proyecto, TareaProyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_finalizacion', 'estado']


class TareaProyectoForm(forms.ModelForm):
    class Meta:
        model = TareaProyecto
        fields = ['proyecto', 'nombre', 'responsable', 'fecha_limite']
