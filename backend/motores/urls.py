from django.urls import path
from .views import (
    # Modelos de Motor
    ModeloMotorListView,
    ModeloMotorCreateView,
    ModeloMotorDetailView,
    
    # Motores
    MotorListView,
    MotorCreateView,
    MotorDetailView,
    MotoresPorUsuarioView,
    MotoresPorModeloView,
    MotoresActivosView
)

urlpatterns = [
    # Modelos de Motor
    path('modelos/', ModeloMotorListView.as_view(), name='modelos-motor-list'),
    path('modelos/crear/', ModeloMotorCreateView.as_view(), name='modelo-motor-create'),
    path('modelos/<int:pk>/', ModeloMotorDetailView.as_view(), name='modelo-motor-detail'),
    
    # Motores
    path('', MotorListView.as_view(), name='motores-list'),
    path('crear/', MotorCreateView.as_view(), name='motor-create'),
    path('activos/', MotoresActivosView.as_view(), name='motores-activos'),
    path('<int:pk>/', MotorDetailView.as_view(), name='motor-detail'),
    path('usuario/<int:usuario_id>/', MotoresPorUsuarioView.as_view(), name='motores-por-usuario'),
    path('modelo/<int:modelo_id>/', MotoresPorModeloView.as_view(), name='motores-por-modelo'),
]