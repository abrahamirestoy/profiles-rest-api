from django.shortcuts import render
#Apartado 8.29
from rest_framework.views import APIView
from rest_framework.response import Response
#Apartado 8.33
from rest_framework import status
from profiles_api import serializers
#Apartado 9.38
from rest_framework import viewsets
#Apartado 10.45
from profiles_api import models
#Apartado 10.49
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
#Apartado 10.51, funcionalidad de rest_framework que permite anyadir filtros
from rest_framework import filters
#Apartado 11.53
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
#Apartado 12.63
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#Apartado 12.65
from rest_framework.permissions import IsAuthenticated

#Apartado 8.29
class HelloApiView(APIView):
    """Test API View"""
    #Apartado 8.33
    serializer_class = serializers.HelloSerializer

    #Apartado 8.29
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put delete)',
            'Is similar to a traditional Django View',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    #Apartado 8.33
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    #Apartado 8.35
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


#Apartado 9.38
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    #Apartado 9.41
    serializer_class = serializers.HelloSerializer

    #Apartado 9.38
    def list(self, request):
        """Return a hello  message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    #Apartado 9.41
    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


#Apartado 10.45
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #Apartado 10.49 Variables de rest_framework que permiten comprobar el autenticado
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    #Apartado 10.51 Variables de rest_framework que permiten realizar la busqueda
    #por name y email.
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


#Apartado 10.53
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



#Apartado 12.61
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    #Apartado 12.63
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
        #Apartado 12.65 sustituir lo anterior por. De esta forma solo pueden
        #leer los estados, usuarios autenticados.
        #IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
