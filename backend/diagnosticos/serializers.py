from rest_framework import serializers
from .models import DiagnosticosTecnicos
from ordenes.models import OrdenesServicio

class DiagnosticoTecnicoSerializer(serializers.ModelSerializer):
    resumen = serializers.ReadOnlyField()
    orden_info = serializers.SerializerMethodField()
    
    class Meta:
        model = DiagnosticosTecnicos
        fields = [
            'id',
            'orden',
            'orden_info',
            'detalle',
            'resumen',
            'creadoen'
        ]
        read_only_fields = ['creadoen']
    
    def get_orden_info(self, obj):
        """Información básica de la orden asociada"""
        return {
            'id': obj.orden.id,
        }


class DiagnosticoTecnicoCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear diagnósticos técnicos"""
    
    class Meta:
        model = DiagnosticosTecnicos
        fields = [
            'orden',
            'detalle'
        ]
    
    def validate_orden(self, value):
        """Validar que la orden exista"""
        if not OrdenesServicio.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La orden especificada no existe")
        return value
    
    def validate_detalle(self, value):
        """Validar que el detalle tenga contenido significativo"""
        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "El detalle debe tener al menos 10 caracteres"
            )
        return value.strip()


class DiagnosticoTecnicoUpdateSerializer(serializers.ModelSerializer):
    """Serializer para actualizar diagnósticos técnicos"""
    
    class Meta:
        model = DiagnosticosTecnicos
        fields = ['detalle']
    
    def validate_detalle(self, value):
        """Validar que el detalle tenga contenido significativo"""
        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "El detalle debe tener al menos 10 caracteres"
            )
        return value.strip()


class DiagnosticoTecnicoListSerializer(serializers.ModelSerializer):
    """Serializer para listar diagnósticos (versión resumida)"""
    resumen = serializers.ReadOnlyField()
    
    class Meta:
        model = DiagnosticosTecnicos
        fields = [
            'id',
            'orden',
            'resumen',
            'creadoen'
        ]