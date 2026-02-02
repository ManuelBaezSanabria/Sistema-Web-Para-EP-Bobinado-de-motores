from django.urls import path
from .views import OrdenListCreateView, OrdenDetailView, OrdenListView

urlpatterns = [
    path('', OrdenListView.as_view(), name='ordenes-list-create'),
    path('<int:pk>/', OrdenDetailView.as_view(), name='orden-detail'),
    path('registro/', OrdenListCreateView.as_view(), name='registro')
]