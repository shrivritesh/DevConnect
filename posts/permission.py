from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Allow only the owner of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user