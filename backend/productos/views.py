from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.db.models import Q, F
from .models import Productos
from .serializers import (
    ProductoSerializer, 
    ProductoCreateSerializer, 
    ProductoUpdateSerializer,
    ProductoStockUpdateSerializer
)


class ProductoListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        productos = Productos.objects.all()
        
        # Filtros
        categoria = request.query_params.get('categoria', None)
        activo = request.query_params.get('activo', None)
        bajo_stock = request.query_params.get('bajo_stock', None)
        search = request.query_params.get('search', None)
        
        if categoria:
            productos = productos.filter(categoria__icontains=categoria)
        
        if activo is not None:
            productos = productos.filter(activo=activo.lower() == 'true')
        
        if bajo_stock == 'true':
            productos = productos.filter(stock__lte=F('stockminimo'))
        
        if search:
            productos = productos.filter(
                Q(nombre__icontains=search) | 
                Q(categoria__icontains=search)
            )
        
        orden = request.query_params.get('orden', '-id')
        productos = productos.order_by(orden)
        
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)


class ProductoCreateView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = ProductoCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            producto = serializer.save()
            warning = serializer.validated_data.pop('_warning', None)
            
            response_data = ProductoSerializer(producto).data
            if warning:
                response_data['warning'] = warning
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoDetailView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            return None

    def get(self, request, pk):
        producto = self.get_object(pk)
        if not producto:
            return Response(
                {"error": "Producto no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    def put(self, request, pk):
        producto = self.get_object(pk)
        if not producto:
            return Response(
                {"error": "Producto no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductoUpdateSerializer(producto, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(ProductoSerializer(producto).data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        producto = self.get_object(pk)
        if not producto:
            return Response(
                {"error": "Producto no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductoUpdateSerializer(producto, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(ProductoSerializer(producto).data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        producto = self.get_object(pk)
        if not producto:
            return Response(
                {"error": "Producto no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        soft_delete = request.query_params.get('soft', 'true')
        
        if soft_delete.lower() == 'true':
            producto.activo = False
            producto.save()
            return Response(
                {"message": "Producto desactivado correctamente"},
                status=status.HTTP_200_OK
            )
        
        producto.delete()
        return Response(
            {"message": "Producto eliminado permanentemente"},
            status=status.HTTP_204_NO_CONTENT
        )


class ProductoStockUpdateView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, pk):
        try:
            producto = Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            return Response(
                {"error": "Producto no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductoStockUpdateSerializer(data=request.data)
        
        if serializer.is_valid():
            cantidad = serializer.validated_data['cantidad']
            operacion = serializer.validated_data['operacion']
            
            stock_anterior = producto.stock
            
            if operacion == 'agregar':
                producto.stock += cantidad
            elif operacion == 'restar':
                if producto.stock < cantidad:
                    return Response(
                        {"error": "Stock insuficiente"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                producto.stock -= cantidad
            elif operacion == 'establecer':
                producto.stock = cantidad
            
            producto.save()
            
            return Response({
                "message": "Stock actualizado correctamente",
                "stock_anterior": stock_anterior,
                "stock_actual": producto.stock,
                "producto": ProductoSerializer(producto).data
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoBajoStockView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        productos = Productos.objects.filter(
            stock__lte=F('stockminimo'),
            activo=True
        ).order_by('stock')
        
        serializer = ProductoSerializer(productos, many=True)
        
        return Response({
            "count": productos.count(),
            "productos": serializer.data
        })


class ProductoCategoriasView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        categorias = Productos.objects.values_list(
            'categoria', 
            flat=True
        ).distinct().order_by('categoria')
        
        categorias = [cat for cat in categorias if cat]
        
        return Response({
            "count": len(categorias),
            "categorias": categorias
        })
