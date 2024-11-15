from django.urls import path
from . import views

urlpatterns = [
    path('ordenes/', views.OrdenList.as_view(), name='orden_list'),
    path('ordenes/<int:pk>/', views.OrdenDetail.as_view(), name='orden_detail'),
]

