
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.mixins import ListModelMixin
from loans.models import Prestamo
from clients.models import Cliente
from .serializers import (
    ClienteSerializer, 
    ClientAccountSerializer, 
    ClientLoansSerializer)
from accounts.models import Cuenta
from .permissions import IsClientOwner
from bank.utils import get_loged_client
from .mixins import MultipleFieldLookupMixin

# Create your views here.

class ClientDetailAPIView(generics.ListAPIView):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        cliente = get_loged_client(self.request)
        return Cliente.objects.filter(pk=cliente.pk)

class ClientAccountAPIView(generics.ListAPIView):
    serializer_class = ClientAccountSerializer
    permission_classes = [IsClientOwner]

    def get_queryset(self):
        cliente = get_loged_client(self.request)
        return Cuenta.objects.filter(customer_id=cliente.pk)

class ClientLoansAPIView(generics.ListAPIView):
    serializer_class = ClientLoansSerializer
    permission_classes = [IsClientOwner]

    def get_queryset(self):
        cliente = get_loged_client(self.request)
        return Prestamo.objects.filter(customer_id=cliente.pk)


# class BranchLoansAPIView(ListModelMixin,generics.GenericAPIView):
#     serializer_class = BranchLoansSerializer
#     permission_classes = [IsAdminUser]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def get_queryset(self):
#         queryset = Prestamo.objects.all()
#         lista = list()
#         clientes = Cliente.objects.filter(branch_id=3)
#         print(clientes)
#         for cliente in clientes:
#             qs = cliente.prestamo_set.all()
#             print(qs)
#             if len(qs) !=0:
#                 lista.append(qs)
#         return queryset.intersection(*lista)
    


class BranchLoansAPIView(generics.ListAPIView):
    serializer_class = ClientLoansSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        branch_id = self.request.parser_context.get("kwargs")
        clientes = Cliente.objects.filter(**branch_id)
        queryset = Prestamo.objects.none()
              
        for cliente in clientes:
            qs = Prestamo.objects.filter(customer_id = cliente.pk)
            if len(qs) !=0:
                qs2 = Prestamo.objects.all().intersection(qs)
                queryset = queryset.union(qs2)

        return queryset