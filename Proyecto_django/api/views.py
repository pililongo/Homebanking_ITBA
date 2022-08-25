from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.mixins import ListModelMixin
from loans.models import Prestamo
from clients.models import Cliente
from .serializers import (
    ClienteSerializer, 
    ClientAccountSerializer, 
    ClientLoansSerializer, 
    BranchLoansSerializer)
from accounts.models import Cuenta
from .permissions import IsClientOwner
from bank.utils import get_loged_client

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


class LoansBranchAPIView(ListModelMixin,generics.GenericAPIView):
    serializer_class = BranchLoansSerializer
    permission_classes = [IsAdminUser]

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = Prestamo.objects.all()
        lista = []
        branch_id = kwargs.get("pk")
        clientes = Cliente.objects.filter(branch_id=branch_id)
        for cliente in clientes:
            lista.append(Prestamo.objects.filter(customer_id=cliente.pk))
        queryset.difference(*lista)
        print(len(queryset))
        return Prestamo.objects.all().difference(queryset)
        


# class LoansBranchAPIView(generics.ListAPIView):
#     serializer_class = BranchLoansSerializer
#     permission_classes = [IsAdminUser]

    