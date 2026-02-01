from rest_framework import serializers
from .models import Usuario, Roles
from django.contrib.auth.hashers import make_password

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'password', 'confirm_password', 'telefono']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')

        rol_cliente, _ = Roles.objects.get_or_create(
            nombre='Cliente',
            defaults={'descripcion': 'Cliente del sistema'}
        )

        usuario = Usuario(
            nombre=validated_data['nombre'],
            email=validated_data['email'],
            telefono=validated_data.get('telefono', ''),
            rol=rol_cliente,
            activo=True
        )
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UsuarioListSerializer(serializers.ModelSerializer):
    rol = serializers.CharField(source='rol.nombre')

    class Meta:
        model = Usuario
        fields = [
            'id',
            'nombre',
            'email',
            'telefono',
            'rol',
            'activo',
            'creadoen'
        ]


class UsuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'telefono', 'activo']
