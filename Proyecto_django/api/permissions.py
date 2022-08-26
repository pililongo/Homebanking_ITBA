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
