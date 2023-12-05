from rest_framework import permissions
class UserPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        # Your custom permission logic here
        return False