from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Read: everyone
    Write/Update/Delete: only seller of the listing
    """

    def has_object_permission(self, request, view, obj):
        # SAFE methods = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.seller == request.user
