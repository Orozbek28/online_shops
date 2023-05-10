from rest_framework import permissions


class AuthTokenPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        elif request.user and request.user.is_authenticated:
            return True
