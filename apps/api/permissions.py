from rest_framework.permissions import BasePermission

# custom permission that allows only company users to access the view;
class IsCompany(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_company:
            return True
        return False