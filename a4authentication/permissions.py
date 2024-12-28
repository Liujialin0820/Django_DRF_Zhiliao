from rest_framework import permissions


class MyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Referer
        referer = request.META.get("HTTP_REFERER")
        print("referer:", referer)
        if referer:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if "长沙" in obj.name:
            return True
        return False
