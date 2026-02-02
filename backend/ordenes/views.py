from django.shortcuts import get_object_or_404, render

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import OrdenCreateSerializer, OrdenListSerializer, OrdenUpdateSerializer
from .models import OrdenesServicio
from rest_framework.permissions import AllowAny


class OrdenListCreateView(generics.CreateAPIView):
    serializer_class = OrdenCreateSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        orden = serializer.save()
        
        return Response({
            'ordenes': {
                'id': orden.id,
                'motorid': orden.motorid.id,
                'estado': orden.estado
            }
        }, status=status.HTTP_201_CREATED)

class OrdenListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        ordenes = OrdenesServicio.objects.all()
        serializer = OrdenListSerializer(ordenes, many=True)
        return Response(serializer.data)

class OrdenDetailView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return OrdenesServicio.objects.get(pk=pk)
        except OrdenesServicio.DoesNotExist:
            return None

    def get(self, request, pk):
        orden = self.get_object(pk)
        if not orden:
            return Response({"error": "Orden no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrdenListSerializer(orden)
        return Response(serializer.data)

    def put(self, request, pk):
        orden = self.get_object(pk)
        if not orden:
            return Response({"error": "Orden no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrdenUpdateSerializer(orden, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(OrdenListSerializer(orden).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        orden = self.get_object(pk)
        if not orden:
            return Response({"error": "Orden no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        orden.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
