#Apartado 10.47, Modulo de permisos de django rest_framework
from rest_framework import permissions

#Apartado 10.47
class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        #Si la peticion se realiza utilizando metodos seguros(get), return True
        #ya que la consulta es solo de lectura.
        if request.method in permissions.SAFE_METHODS:
            return True
        #Si la peticion no es a traves de un metodo seguro(POST,UPDATE,..)
        #Return True solo si el objeto a tratar pertenece al usuario autenticado.
        return obj.id == request.user.id
