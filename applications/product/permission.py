from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    # CREATE,LIST
    def has_permission(self, request, view):
        if request.method =='GET':
            return True
        return request.user.is_authenticated and request.user.is_staff


    # RETRIEVE,UPDATE,DELETE
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  #GET, OPTION, HEAD
            return True
        return request.user.is_authenticated and request.user.is_staff


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        # print(dir(obj))
        return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)

