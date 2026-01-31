from django.shortcuts import render
from .models import Proveedores
from rest_framework import generics
from .serializers import ProveedoresSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateProveedorView(generics.CreateAPIView):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer
    permission_classes = [AllowAny]
