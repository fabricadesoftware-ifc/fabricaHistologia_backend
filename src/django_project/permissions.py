from rest_framework.permissions import BasePermission, SAFE_METHODS


class customDefaultPermission(BasePermission):
 
    def has_permission(self, request, view):
        # Allow read-only access for safe methods
        if request.method in SAFE_METHODS:
            return True

        # Allow write access for authenticated users
        return request.user and request.user.is_authenticated and request.user.is_verified or request.user.is_superuser
    
class customDataPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return request.user and request.user.is_authenticated and request.user.is_verified
        return request.user and request.user.is_superuser
        
class customVerifiedPermission(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_verified or request.user.is_superuser