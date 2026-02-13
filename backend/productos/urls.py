from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoDetailView,
    ProductoStockUpdateView,
    ProductoBajoStockView,
    ProductoCategoriasView
)

urlpatterns = [
    path('', ProductoListView.as_view(), name='productos-list'),
    path('crear/', ProductoCreateView.as_view(), name='producto-create'),
    path('bajo-stock/', ProductoBajoStockView.as_view(), name='productos-bajo-stock'),
    path('categorias/', ProductoCategoriasView.as_view(), name='productos-categorias'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('<int:pk>/stock/', ProductoStockUpdateView.as_view(), name='producto-stock-update'),
]