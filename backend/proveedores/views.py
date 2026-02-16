from django.shortcuts import render
from .models import Proveedores
from .serializers import ProveedoresSerializer, ProveedoresListSerializer, ProveedoresDetailSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateProveedorView(generics.CreateAPIView):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer
    permission_classes = [AllowAny]

class ProveedorListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        proveedores = Proveedores.objects.all()
        serializer_class = ProveedoresListSerializer(proveedores, many=True)
        return Response(serializer_class.data)

class ProveedorDetailView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return None

    def get(self, request, pk):
        proveedor = self.get_object(pk)
        if not proveedor:
            return Response(
                {"error": "Proveedor no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer_class = ProveedoresListSerializer(proveedor)
        return Response(serializer_class.data)

    def put(self, request, pk):
        proveedor = self.get_object(pk)
        if not proveedor:
            return Response({"error": "Proveedor no encontrado"}, status=404)

        serializer_class = ProveedoresDetailSerializer(proveedor, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)

        return Response(serializer_class.errors, status=400)

    def delete(self, request, pk):
        proveedor = self.get_object(pk)
        if not proveedor:
            return Response({"error": "Proveedor no encontrado"}, status=404)

        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)