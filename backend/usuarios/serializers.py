from rest_framework import serializers
from .models import Usuario, Roles
from django.contrib.auth.hashers import make_password

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)
    rol = serializers.CharField(write_only=True)
    cedula = serializers.CharField(required=True, max_length=20)  # Campo obligatorio

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'password', 'confirm_password', 'telefono', 'cedula', 'rol']


    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        rol_nombre = validated_data.pop('rol')
        rol_obj, _ = Roles.objects.get_or_create(nombre=rol_nombre)  

        if 'username' not in validated_data:
            validated_data['username'] = validated_data['email'].split('@')[0]

        usuario = Usuario(
            nombre=validated_data['nombre'],
            email=validated_data['email'],
            telefono=validated_data.get('telefono', ''),
            cedula=validated_data['cedula'],
            rol=rol_obj,
            username=validated_data['username'],
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
