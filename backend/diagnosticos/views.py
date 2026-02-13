from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.db.models import Q

from .models import DiagnosticosTecnicos
from ordenes.models import OrdenesServicio 
from .serializers import (
    DiagnosticoTecnicoSerializer,
    DiagnosticoTecnicoCreateSerializer,
    DiagnosticoTecnicoUpdateSerializer,
    DiagnosticoTecnicoListSerializer
)


class DiagnosticoTecnicoListView(APIView):
    """Lista todos los diagnósticos técnicos con filtros opcionales"""
    permission_classes = [AllowAny]

    def get(self, request):
        diagnosticos = DiagnosticosTecnicos.objects.all()
        
        # Filtros opcionales
        orden_id = request.query_params.get('orden_id', None)
        fecha_desde = request.query_params.get('fecha_desde', None)
        fecha_hasta = request.query_params.get('fecha_hasta', None)
        search = request.query_params.get('search', None)
        
        if orden_id:
            diagnosticos = diagnosticos.filter(orden_id=orden_id)
        
        if fecha_desde:
            diagnosticos = diagnosticos.filter(creadoen__gte=fecha_desde)
        
        if fecha_hasta:
            diagnosticos = diagnosticos.filter(creadoen__lte=fecha_hasta)
        
        if search:
            diagnosticos = diagnosticos.filter(detalle__icontains=search)
        
        # Ordenar
        orden = request.query_params.get('orden', '-creadoen')
        diagnosticos = diagnosticos.order_by(orden)
        
        # Usar serializer resumido o completo según parámetro
        resumido = request.query_params.get('resumido', 'false')
        if resumido.lower() == 'true':
            serializer = DiagnosticoTecnicoListSerializer(diagnosticos, many=True)
        else:
            serializer = DiagnosticoTecnicoSerializer(diagnosticos, many=True)
        
        return Response({
            'count': diagnosticos.count(),
            'diagnosticos': serializer.data
        })


class DiagnosticoTecnicoCreateView(APIView):
    """Crear un nuevo diagnóstico técnico"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = DiagnosticoTecnicoCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            diagnostico = serializer.save()
            
            return Response(
                DiagnosticoTecnicoSerializer(diagnostico).data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DiagnosticoTecnicoDetailView(APIView):
    """Ver, actualizar o eliminar un diagnóstico técnico específico"""
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return DiagnosticosTecnicos.objects.get(pk=pk)
        except DiagnosticosTecnicos.DoesNotExist:
            return None

    def get(self, request, pk):
        """Obtener detalle de un diagnóstico técnico"""
        diagnostico = self.get_object(pk)
        if not diagnostico:
            return Response(
                {"error": "Diagnóstico técnico no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = DiagnosticoTecnicoSerializer(diagnostico)
        return Response(serializer.data)

    def put(self, request, pk):
        """Actualizar un diagnóstico técnico"""
        diagnostico = self.get_object(pk)
        if not diagnostico:
            return Response(
                {"error": "Diagnóstico técnico no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = DiagnosticoTecnicoUpdateSerializer(
            diagnostico, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(DiagnosticoTecnicoSerializer(diagnostico).data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        """Actualizar parcialmente un diagnóstico técnico"""
        diagnostico = self.get_object(pk)
        if not diagnostico:
            return Response(
                {"error": "Diagnóstico técnico no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = DiagnosticoTecnicoUpdateSerializer(
            diagnostico, 
            data=request.data, 
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(DiagnosticoTecnicoSerializer(diagnostico).data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """Eliminar un diagnóstico técnico"""
        diagnostico = self.get_object(pk)
        if not diagnostico:
            return Response(
                {"error": "Diagnóstico técnico no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        diagnostico.delete()
        return Response(
            {"message": "Diagnóstico técnico eliminado correctamente"},
            status=status.HTTP_204_NO_CONTENT
        )


class DiagnosticosPorOrdenView(APIView):
    """Obtener todos los diagnósticos de una orden específica"""
    permission_classes = [AllowAny]
    
    def get(self, request, orden_id):
        # Verificar que la orden existe
        try:
            orden = OrdenesServicio.objects.get(id=orden_id)
        except OrdenesServicio.DoesNotExist:
            return Response(
                {"error": "Orden no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        diagnosticos = DiagnosticosTecnicos.objects.filter(orden_id=orden_id)
        serializer = DiagnosticoTecnicoSerializer(diagnosticos, many=True)
        
        return Response({
            'orden_id': orden_id,
            'count': diagnosticos.count(),
            'diagnosticos': serializer.data
        })


class DiagnosticosRecientesView(APIView):
    """Obtener los diagnósticos más recientes"""
    permission_classes = [AllowAny]
    
    def get(self, request):
        limite = request.query_params.get('limite', 10)
        try:
            limite = int(limite)
            if limite > 100:
                limite = 100
        except ValueError:
            limite = 10
        
        diagnosticos = DiagnosticosTecnicos.objects.all()[:limite]
        serializer = DiagnosticoTecnicoListSerializer(diagnosticos, many=True)
        
        return Response({
            'count': diagnosticos.count(),
            'diagnosticos': serializer.data
        })
