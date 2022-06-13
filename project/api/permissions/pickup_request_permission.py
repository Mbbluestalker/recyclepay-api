from rest_framework.permissions import BasePermission


class IsIndividualOrParner(BasePermission):

    def has_permission(self, request, view):
        return bool((request.user and request.user.is_authenticated) and (request.user.is_partner or request.user.is_individual))