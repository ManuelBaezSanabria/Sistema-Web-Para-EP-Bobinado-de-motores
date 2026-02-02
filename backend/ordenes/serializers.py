from rest_framework import serializers
from .models import OrdenesServicio


class OrdenCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdenesServicio
        fields = ['motorid', 'estado']


class OrdenListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdenesServicio
        fields = ['id','motorid', 'estado', 'tecnicoid', 'creadoen']


class OrdenUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenesServicio
        fields = ['estado', 'tecnicoid']