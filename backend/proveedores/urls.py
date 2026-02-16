from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateProveedorView.as_view()),
    path("list/", views.ProveedorListView.as_view()),
    path('<int:pk>/', views.ProveedorDetailView.as_view()),
]
