from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user or (request.method in SAFE_METHODS):
            return True
        return False
