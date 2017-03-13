from rest_framework import permissions
from app.url import Urls

class PermissionLevel(permissions.BasePermission):
    """
    Permisos para los request
    """

    def has_permission(self, request, view):

        if Urls(request.path_info).isSafe:
            return True

        return True
