
from rest_framework.permissions import BasePermission
from bank.utils import get_loged_client

class IsAuthenticatedClient(BasePermission):
    def has_object_permission(self, request, view, obj):
        cliente = get_loged_client(request)
        return cliente.pk == obj.pk

class IsClientOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        cliente = get_loged_client(request)
        return cliente.pk == obj.customer_id

class IsStaffOrClient(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        cliente = get_loged_client(request)
        return cliente.address_id.pk == obj.address_id
    