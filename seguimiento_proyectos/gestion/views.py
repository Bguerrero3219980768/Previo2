from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto, TareaProyecto
from .form import ProyectoForm, TareaProyectoForm

# Proyectos
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'gestion/proyecto_lista.html', {'proyectos': proyectos})

def detalle_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'gestion/proyecto_detalle.html', {'proyecto': proyecto})

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'gestion/proyecto_form.html', {'form': form})

def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'gestion/proyecto_form.html', {'form': form})

def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'gestion/proyecto_confirmar_eliminar.html', {'proyecto': proyecto})

# Tareas
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = TareaProyectoForm()
    return render(request, 'gestion/tarea_form.html', {'form': form})
