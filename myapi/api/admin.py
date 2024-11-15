from django.contrib import admin
from .models import Orden, DetalleOrden

class DetalleOrdenInline(admin.TabularInline):
    model = DetalleOrden
    extra = 1

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    inlines = [DetalleOrdenInline]
    list_display = ('numero_orden', 'fecha', 'estado', 'total')
    list_filter = ('estado', 'fecha')
    search_fields = ('numero_orden',)
