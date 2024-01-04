from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:     # CHECK IF THE REQUEST IS SAFE (GET, POST)
            return True

        # CHECK IF AUTHENTICATED USER MATCH THE USER
        return obj.id == request.user.id