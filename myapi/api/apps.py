from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import DetalleOrden

@receiver(post_save, sender=DetalleOrden)
@receiver(post_delete, sender=DetalleOrden)
def actualizar_total(sender, instance, **kwargs):
    orden = instance.orden
    orden.save()
def save(self, *args, **kwargs):
    self.total = sum([detalle.subtotal() for detalle in self.detalles.all()])
    super().save(*args, **kwargs)
