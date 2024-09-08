from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to modify only their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Checking user is trying to update their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.id == obj.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update status """

    def has_object_permission(self, request, view, obj):
        """Checking user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id
