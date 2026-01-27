from django.shortcuts import render

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import RegistroSerializer, LoginSerializer
from .models import Usuario

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
