from rest_framework.permissions import BasePermission


class IsHospital(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'HOSPITAL'


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'ADMIN'


class IsDriver(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'DRIVER'
