from django.urls import path
from .views import (
    DiagnosticoTecnicoListView,
    DiagnosticoTecnicoCreateView,
    DiagnosticoTecnicoDetailView,
    DiagnosticosPorOrdenView,
    DiagnosticosRecientesView
)

urlpatterns = [
    
    # Diagnósticos Técnicos
    path('diagnosticos/', DiagnosticoTecnicoListView.as_view(), name='diagnosticos-list'),
    path('diagnosticos/crear/', DiagnosticoTecnicoCreateView.as_view(), name='diagnostico-create'),
    path('diagnosticos/recientes/', DiagnosticosRecientesView.as_view(), name='diagnosticos-recientes'),
    path('diagnosticos/<int:pk>/', DiagnosticoTecnicoDetailView.as_view(), name='diagnostico-detail'),
    path('diagnosticos/orden/<int:orden_id>/', DiagnosticosPorOrdenView.as_view(), name='diagnosticos-por-orden'),
]