from django.urls import path
from . import views

urlpatterns = [
    path("proveedores/", views.CreateProveedorView.as_view(), name="proveedores"),
]
