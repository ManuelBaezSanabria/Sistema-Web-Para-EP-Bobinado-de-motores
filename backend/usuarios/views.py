from django.shortcuts import get_object_or_404, render

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import RegistroSerializer, LoginSerializer, UsuarioListSerializer, UsuarioUpdateSerializer
from .models import Usuario
from rest_framework.permissions import AllowAny


class RegistroView(generics.CreateAPIView):
    serializer_class = RegistroSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        
        # Crear token para el usuario
        token, created = Token.objects.get_or_create(user=usuario)
        
        return Response({
            'token': token.key,
            'usuario': {
                'id': usuario.id,
                'nombre': usuario.nombre,
                'email': usuario.email,
                'rol': usuario.rol.nombre
            }
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            user = authenticate(request, email=email, password=password)
            
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'usuario': {
                        'id': user.id,
                        'nombre': user.nombre,
                        'email': user.email,
                        'rol': user.rol.nombre
                    }
                })
            return Response({'error': 'Credenciales inválidas'}, status=400)
        return Response(serializer.errors, status=400)

class UsuarioListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioListSerializer(usuarios, many=True)
        return Response(serializer.data)


class UsuarioDetailView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return None

    def get(self, request, pk):
        usuario = self.get_object(pk)
        if not usuario:
            return Response(
                {"error": "Usuario no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UsuarioListSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk):
        usuario = self.get_object(pk)
        if not usuario:
            return Response({"error": "Usuario no encontrado"}, status=404)

        serializer = UsuarioUpdateSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        usuario = self.get_object(pk)
        if not usuario:
            return Response({"error": "Usuario no encontrado"}, status=404)

        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
