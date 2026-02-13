from rest_framework import serializers
from .models import OrdenesServicio

class OrdenCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenesServicio
        fields = ['motorid', 'estado']

class OrdenListSerializer(serializers.ModelSerializer):
    motor_info = serializers.SerializerMethodField()
    tecnico_nombre = serializers.CharField(source='tecnicoid.nombre', read_only=True, allow_null=True)
    
    class Meta:
        model = OrdenesServicio
        fields = ['id', 'motorid', 'motor_info', 'estado', 'tecnicoid', 'tecnico_nombre', 'creadoen']
    
    def get_motor_info(self, obj):
        return {
            'id': obj.motorid.id,
            'modelo': obj.motorid.modelo.nombre,
            'serie': obj.motorid.numeroserie
        }

class OrdenUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenesServicio
        fields = ['estado', 'tecnicoid']