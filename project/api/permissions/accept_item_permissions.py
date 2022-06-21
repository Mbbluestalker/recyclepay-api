from rest_framework.permissions import BasePermission


class IsCollector(BasePermission):
    """
    Allows access only to the Collector only.
    """

    def has_permission(self, request, view):
        return bool(request.user
                    and request.user.is_authenticated
                    and request.user.is_collector)
