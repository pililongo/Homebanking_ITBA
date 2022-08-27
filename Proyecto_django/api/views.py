from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from loans.models import Prestamo
from clients.models import Cliente
from .serializers import (
    ClienteSerializer, 
    ClientAccountSerializer, 
    ClientLoansSerializer,
    CardsSerializer,
    BranchSerializer,
    AddressSerializer,
    LoansSerializer)
from accounts.models import Cuenta
from .permissions import IsClientOwner, IsStaffOrClient
from bank.utils import get_loged_client
from bank.models import Sucursal, Direcciones
from rest_framework.exceptions import ValidationError

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

class CardsAPIView(generics.ListAPIView):
    serializer_class = CardsSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        client_id = self.request.parser_context.get("kwargs")
        cliente = Cliente.objects.filter(**client_id).first()
        return cliente.tarjeta_set.all()

class LoanCreateAPIView(generics.CreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = LoansSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        client_id = self.request.parser_context.get("kwargs")
        cliente = Cliente.objects.filter(**client_id).first()
        ammount = serializer.validated_data.get('loan_total')
        account = cliente.cuenta_set.filter(cuenta_id = 1).first()
        if account:
            serializer.save(customer_id = cliente)
            account.balance += ammount
            account.save()
        else:
            raise ValidationError('Este cliente no posee caja de ahorro en pesos')

class LoanDestroyAPIView(generics.DestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = LoansSerializer
    permission_classes = [IsAdminUser]

    def perform_destroy(self, instance):
        ammount = instance.loan_total
        cliente = instance.customer_id
        account = cliente.cuenta_set.filter(cuenta_id = 1).first()
        account.balance -= ammount
        account.save()
        super().perform_destroy(instance)

class AddressAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = AddressSerializer
    queryset = Direcciones.objects.all()
    permission_classes = [IsStaffOrClient]

    def perform_update(self, serializer):
        serializer.save()

class BranchAPIView(generics.ListAPIView):
    serializer_class = BranchSerializer
    permission_classes = []
    authentication_classes = []
    queryset = Sucursal.objects.all()