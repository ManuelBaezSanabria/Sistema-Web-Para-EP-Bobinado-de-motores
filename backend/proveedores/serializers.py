from rest_framework import serializers
import django.contrib.auth.models
from .models import Proveedores

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = ["id", "nombre", "contacto", "creadopor", "fechacreacion"]
        extra_kwargs = {"creadopor": {"read_only": True}}

    def create(self, validated_data):
        print(validated_data)
        proveedor = Proveedores.objects.create(**validated_data)
        return proveedor


class ProveedoresListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedores
        fields = [
            'id',
            'nombre',
            'contacto',
            'creadopor',
            'fechacreacion'
        ]

class ProveedoresDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = ['nombre', 'contacto', 'creadopor', 'fechacreacion']