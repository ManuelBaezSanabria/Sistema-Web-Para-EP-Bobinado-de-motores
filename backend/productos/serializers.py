from rest_framework import serializers
from .models import Productos

class ProductoSerializer(serializers.ModelSerializer):
    necesita_reposicion = serializers.ReadOnlyField()
    
    class Meta:
        model = Productos
        fields = [
            'id',
            'nombre',
            'categoria',
            'stock',
            'stockminimo',
            'precio',
            'activo',
            'necesita_reposicion'
        ]
    
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo")
        return value
    
    def validate_stockminimo(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock mínimo no puede ser negativo")
        return value
    
    def validate_precio(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("El precio no puede ser negativo")
        return value


class ProductoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = [
            'nombre',
            'categoria',
            'stock',
            'stockminimo',
            'precio',
            'activo'
        ]
    
    def validate(self, data):
        if data.get('stock', 0) < data.get('stockminimo', 0):
            data['_warning'] = "El stock inicial es menor al stock mínimo"
        return data


class ProductoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = [
            'nombre',
            'categoria',
            'stock',
            'stockminimo',
            'precio',
            'activo'
        ]
        extra_kwargs = {
            'nombre': {'required': False},
            'categoria': {'required': False},
            'stock': {'required': False},
            'stockminimo': {'required': False},
            'precio': {'required': False},
            'activo': {'required': False}
        }


class ProductoStockUpdateSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    operacion = serializers.ChoiceField(choices=['agregar', 'restar', 'establecer'])
    
    def validate_cantidad(self, value):
        if value < 0:
            raise serializers.ValidationError("La cantidad no puede ser negativa")
        return value