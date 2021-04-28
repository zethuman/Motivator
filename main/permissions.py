from rest_framework.permissions import IsAuthenticated,IsAdminUser

from books_module.models import BookMotivator
from utils.constants import USER_ROLE_HR,USER_ROLE_EMPLOYEE,USER_ROLE_SUPER_USER


class HrPermission(IsAuthenticated):
    message = "You are not staff"

    def has_permission(self, request, view):
        if request.method == 'GET':
            return super().has_permission(request, view) and request.user.role == USER_ROLE_HR or request.user.role == USER_ROLE_SUPER_USER
        if request.method == 'DELETE':
            return super().has_permission(request, view) and request.user.role == USER_ROLE_SUPER_USER
        else:
            return True


class EmployeePermission(IsAuthenticated):
    message = "You are not employee"

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_EMPLOYEE


class AdminPermission(IsAuthenticated):
    message = "You are not admin"

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_SUPER_USER


class MyCustomPermission(IsAdminUser):
    message = "You are not admin"

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return super().has_permission(request, view) and request.user.role == USER_ROLE_SUPER_USER


class CurrentUserPermission(IsAuthenticated, ):
    message = "You can not change information about others"

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return super().has_permission(request, view) and view.queryset.model('user_id').user_id == request.user.pk



# class ConstraintPermission(IsAuthenticated, ):
#     message = "You can not post more than 3 books"
#
#     def has_permission(self, request, view):
#         return super().has_permission(request, view) and \
#                request.user.books.count() > BookMotivator.objects.filter(user_id = request.user.id)[0].counter
