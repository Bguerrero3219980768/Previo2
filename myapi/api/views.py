from rest_framework import generics
from .models import Orden
from .serializers import OrdenSerializer

# Vista para listar y crear órdenes
class OrdenList(generics.ListCreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

# Vista para recuperar, actualizar y eliminar una orden específica
class OrdenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

