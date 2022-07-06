from rest_framework.permissions import BasePermission


class IsCompany(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_company:
            return True
        return False