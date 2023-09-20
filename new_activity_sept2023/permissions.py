# Django and DRF imports
from rest_framework.permissions import BasePermission


class IsUserDniAndIsAuthenticatedCar(BasePermission):

    def has_permission(self, request, view):

        return bool(request.user and request.user.is_authenticated and request.user.dni)


class IsUserIsStaffAndIsAuthenticatedWorker(BasePermission):

    def has_permission(self, request, view):

        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


class IsUserDniAndIsStaffAndIsAuthenticatedWorkshop(BasePermission):

    def has_permission(self, request, view):

        return bool(request.user and request.user.is_authenticated and request.user.dni and request.user.is_staff)


class IsUserDniAndPhoneNumberAndIsAuthenticatedRepair(BasePermission):

    def has_permission(self, request, view):

        return bool(request.user and request.user.is_authenticated and request.user.dni and request.user.phone)
