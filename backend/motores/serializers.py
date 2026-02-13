from rest_framework import serializers
from .models import ModelosMotor, Motores
from usuarios.models import Usuario


# ========================
# SERIALIZERS PARA MODELOS DE MOTOR
# ========================

class ModeloMotorSerializer(serializers.ModelSerializer):
    cantidad_motores = serializers.SerializerMethodField()
    
    class Meta:
        model = ModelosMotor
        fields = [
            'id',
            'nombre',
            'especificaciones',
            'cantidad_motores'
        ]
    
    def get_cantidad_motores(self, obj):
        """Cantidad de motores de este modelo"""
        return obj.motores.count()


class ModeloMotorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelosMotor
        fields = ['nombre', 'especificaciones']
    
    def validate_nombre(self, value):
        """Validar que el nombre no esté duplicado"""
        if ModelosMotor.objects.filter(nombre__iexact=value).exists():
            raise serializers.ValidationError(
                "Ya existe un modelo de motor con este nombre"
            )
        return value.strip()


class ModeloMotorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelosMotor
        fields = ['nombre', 'especificaciones']
        extra_kwargs = {
            'nombre': {'required': False},
            'especificaciones': {'required': False}
        }
    
    def validate_nombre(self, value):
        """Validar que el nombre no esté duplicado (excluyendo el actual)"""
        modelo_id = self.instance.id if self.instance else None
        if ModelosMotor.objects.filter(nombre__iexact=value).exclude(id=modelo_id).exists():
            raise serializers.ValidationError(
                "Ya existe un modelo de motor con este nombre"
            )
        return value.strip()


# ========================
# SERIALIZERS PARA MOTORES
# ========================

class MotorSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.nombre', read_only=True)
    usuario_email = serializers.EmailField(source='usuario.email', read_only=True)
    usuario_telefono = serializers.CharField(source='usuario.telefono', read_only=True)
    usuario_cedula = serializers.CharField(source='usuario.cedula', read_only=True)
    modelo_nombre = serializers.CharField(source='modelo.nombre', read_only=True)
    modelo_especificaciones = serializers.CharField(source='modelo.especificaciones', read_only=True)
    info_completa = serializers.ReadOnlyField()
    
    class Meta:
        model = Motores
        fields = [
            'id',
            'usuario',
            'usuario_nombre',
            'usuario_email',
            'usuario_telefono',
            'usuario_cedula',
            'modelo',
            'modelo_nombre',
            'modelo_especificaciones',
            'numeroserie',
            'creadoen',
            'info_completa'
        ]
        read_only_fields = ['creadoen']


class MotorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motores
        fields = [
            'usuario',
            'modelo',
            'numeroserie'
        ]
    
    def validate_usuario(self, value):
        """Validar que el usuario exista y esté activo"""
        try:
            usuario = Usuario.objects.get(id=value.id)
            if not usuario.activo:
                raise serializers.ValidationError(
                    "El usuario seleccionado está inactivo"
                )
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("El usuario especificado no existe")
        return value
    
    def validate_modelo(self, value):
        """Validar que el modelo exista"""
        if not ModelosMotor.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El modelo especificado no existe")
        return value
    
    def validate_numeroserie(self, value):
        """Validar que el número de serie sea único si se proporciona"""
        if value:
            value = value.strip()
            if Motores.objects.filter(numeroserie__iexact=value).exists():
                raise serializers.ValidationError(
                    "Ya existe un motor con este número de serie"
                )
        return value


class MotorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motores
        fields = [
            'usuario',
            'modelo',
            'numeroserie'
        ]
        extra_kwargs = {
            'usuario': {'required': False},
            'modelo': {'required': False},
            'numeroserie': {'required': False}
        }
    
    def validate_usuario(self, value):
        """Validar que el usuario exista y esté activo"""
        try:
            usuario = Usuario.objects.get(id=value.id)
            if not usuario.activo:
                raise serializers.ValidationError(
                    "El usuario seleccionado está inactivo"
                )
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("El usuario especificado no existe")
        return value
    
    def validate_numeroserie(self, value):
        """Validar que el número de serie sea único (excluyendo el actual)"""
        if value:
            value = value.strip()
            motor_id = self.instance.id if self.instance else None
            if Motores.objects.filter(numeroserie__iexact=value).exclude(id=motor_id).exists():
                raise serializers.ValidationError(
                    "Ya existe un motor con este número de serie"
                )
        return value


class MotorListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listados"""
    usuario_nombre = serializers.CharField(source='usuario.nombre', read_only=True)
    modelo_nombre = serializers.CharField(source='modelo.nombre', read_only=True)
    
    class Meta:
        model = Motores
        fields = [
            'id',
            'usuario_nombre',
            'modelo_nombre',
            'numeroserie',
            'creadoen'
        ]