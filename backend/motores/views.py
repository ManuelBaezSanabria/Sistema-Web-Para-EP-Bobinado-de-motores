from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.db.models import Q, Count
from .models import ModelosMotor, Motores
from usuarios.models import Usuario
from .serializers import (
    ModeloMotorSerializer,
    ModeloMotorCreateSerializer,
    ModeloMotorUpdateSerializer,
    MotorSerializer,
    MotorCreateSerializer,
    MotorUpdateSerializer,
    MotorListSerializer
)


# ========================
# VISTAS PARA MODELOS DE MOTOR
# ========================

class ModeloMotorListView(APIView):
    """Lista todos los modelos de motor con filtros opcionales"""
    permission_classes = [AllowAny]

    def get(self, request):
        modelos = ModelosMotor.objects.all()
        
        # Filtros
        search = request.query_params.get('search', None)
        
        if search:
            modelos = modelos.filter(
                Q(nombre__icontains=search) | 
                Q(especificaciones__icontains=search)
            )
        
        # Ordenar
        orden = request.query_params.get('orden', 'nombre')
        modelos = modelos.order_by(orden)
        
        # Anotar con cantidad de motores
        modelos = modelos.annotate(cantidad_motores=Count('motores'))
        
        serializer = ModeloMotorSerializer(modelos, many=True)
        
        return Response({
            'count': modelos.count(),
            'modelos': serializer.data
        })


class ModeloMotorCreateView(APIView):
    """Crear un nuevo modelo de motor"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = ModeloMotorCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            modelo = serializer.save()
            
            return Response(
                ModeloMotorSerializer(modelo).data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ModeloMotorDetailView(APIView):
    """Ver, actualizar o eliminar un modelo de motor específico"""
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return ModelosMotor.objects.get(pk=pk)
        except ModelosMotor.DoesNotExist:
            return None

    def get(self, request, pk):
        """Obtener detalle de un modelo de motor"""
        modelo = self.get_object(pk)
        if not modelo:
            return Response(
                {"error": "Modelo de motor no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ModeloMotorSerializer(modelo)
        return Response(serializer.data)

    def put(self, request, pk):
        """Actualizar un modelo de motor"""
        modelo = self.get_object(pk)
        if not modelo:
            return Response(
                {"error": "Modelo de motor no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ModeloMotorUpdateSerializer(modelo, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(ModeloMotorSerializer(modelo).data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        """Actualizar parcialmente un modelo de motor"""
        modelo = self.get_object(pk)
        if not modelo:
            return Response(
                {"error": "Modelo de motor no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ModeloMotorUpdateSerializer(
            modelo, 
            data=request.data, 
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(ModeloMotorSerializer(modelo).data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """Eliminar un modelo de motor"""
        modelo = self.get_object(pk)
        if not modelo:
            return Response(
                {"error": "Modelo de motor no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Verificar si hay motores usando este modelo
        if modelo.motores.exists():
            return Response(
                {
                    "error": "No se puede eliminar el modelo",
                    "detalle": f"Existen {modelo.motores.count()} motores usando este modelo"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        modelo.delete()
        return Response(
            {"message": "Modelo de motor eliminado correctamente"},
            status=status.HTTP_204_NO_CONTENT
        )


# ========================
# VISTAS PARA MOTORES
# ========================

class MotorListView(APIView):
    """Lista todos los motores con filtros opcionales"""
    permission_classes = [AllowAny]

    def get(self, request):
        motores = Motores.objects.select_related('usuario', 'modelo').all()
        
        # Filtros
        usuario_id = request.query_params.get('usuario_id', None)
        modelo_id = request.query_params.get('modelo_id', None)
        search = request.query_params.get('search', None)
        fecha_desde = request.query_params.get('fecha_desde', None)
        fecha_hasta = request.query_params.get('fecha_hasta', None)
        
        if usuario_id:
            motores = motores.filter(usuario_id=usuario_id)
        
        if modelo_id:
            motores = motores.filter(modelo_id=modelo_id)
        
        if search:
            motores = motores.filter(
                Q(numeroserie__icontains=search) |
                Q(usuario__nombre__icontains=search) |
                Q(usuario__email__icontains=search) |
                Q(modelo__nombre__icontains=search)
            )
        
        if fecha_desde:
            motores = motores.filter(creadoen__gte=fecha_desde)
        
        if fecha_hasta:
            motores = motores.filter(creadoen__lte=fecha_hasta)
        
        # Ordenar
        orden = request.query_params.get('orden', '-creadoen')
        motores = motores.order_by(orden)
        
        # Usar serializer resumido o completo
        resumido = request.query_params.get('resumido', 'false')
        if resumido.lower() == 'true':
            serializer = MotorListSerializer(motores, many=True)
        else:
            serializer = MotorSerializer(motores, many=True)
        
        return Response({
            'count': motores.count(),
            'motores': serializer.data
        })


class MotorCreateView(APIView):
    """Crear un nuevo motor"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = MotorCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            motor = serializer.save()
            
            return Response(
                MotorSerializer(motor).data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class MotorDetailView(APIView):
    """Ver, actualizar o eliminar un motor específico"""
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Motores.objects.select_related('usuario', 'modelo').get(pk=pk)
        except Motores.DoesNotExist:
            return None

    def get(self, request, pk):
        """Obtener detalle de un motor"""
        motor = self.get_object(pk)
        if not motor:
            return Response(
                {"error": "Motor no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = MotorSerializer(motor)
        return Response(serializer.data)

    def put(self, request, pk):
        """Actualizar un motor"""
        motor = self.get_object(pk)
        if not motor:
            return Response(
                {"error": "Motor no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = MotorUpdateSerializer(motor, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(MotorSerializer(motor).data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        """Actualizar parcialmente un motor"""
        motor = self.get_object(pk)
        if not motor:
            return Response(
                {"error": "Motor no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = MotorUpdateSerializer(
            motor, 
            data=request.data, 
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(MotorSerializer(motor).data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """Eliminar un motor"""
        motor = self.get_object(pk)
        if not motor:
            return Response(
                {"error": "Motor no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        motor.delete()
        return Response(
            {"message": "Motor eliminado correctamente"},
            status=status.HTTP_204_NO_CONTENT
        )


class MotoresPorUsuarioView(APIView):
    """Obtener todos los motores de un usuario específico"""
    permission_classes = [AllowAny]
    
    def get(self, request, usuario_id):
        # Verificar que el usuario existe
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return Response(
                {"error": "Usuario no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        motores = Motores.objects.filter(usuario_id=usuario_id).select_related('modelo')
        serializer = MotorSerializer(motores, many=True)
        
        return Response({
            'usuario_id': usuario_id,
            'usuario_nombre': usuario.nombre,
            'count': motores.count(),
            'motores': serializer.data
        })


class MotoresPorModeloView(APIView):
    """Obtener todos los motores de un modelo específico"""
    permission_classes = [AllowAny]
    
    def get(self, request, modelo_id):
        # Verificar que el modelo existe
        try:
            modelo = ModelosMotor.objects.get(id=modelo_id)
        except ModelosMotor.DoesNotExist:
            return Response(
                {"error": "Modelo no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        motores = Motores.objects.filter(modelo_id=modelo_id).select_related('usuario')
        serializer = MotorSerializer(motores, many=True)
        
        return Response({
            'modelo_id': modelo_id,
            'modelo_nombre': modelo.nombre,
            'count': motores.count(),
            'motores': serializer.data
        })


class MotoresActivosView(APIView):
    """Obtener motores de usuarios activos"""
    permission_classes = [AllowAny]
    
    def get(self, request):
        motores = Motores.objects.filter(
            usuario__activo=True
        ).select_related('usuario', 'modelo')
        
        serializer = MotorSerializer(motores, many=True)
        
        return Response({
            'count': motores.count(),
            'motores': serializer.data
        })