from dataclasses import field, fields
from rest_framework import serializers
from loans.models import Prestamo
from clients.models import Cliente
from accounts.models import Cuenta
from bank.utils import get_loged_user
from cards.models import Tarjeta
from bank.models import Sucursal, Direcciones


class ClienteSerializer(serializers.ModelSerializer):
    birthday = serializers.CharField(source="dob", read_only=True)
    dni = serializers.CharField(source="customer_dni", read_only=True)
    address = serializers.SerializerMethodField(read_only=True)
    fullname = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cliente
        fields = [
            "fullname",
            "birthday",
            "dni",
            "address",
            "email"
        ]

    def get_address(self, obj):
        return f"{obj.address_id.street} {str(obj.address_id.number)}, {obj.address_id.city}, {obj.address_id.country}"

    def get_fullname(self, obj):
        return f"{obj.customer_name} {obj.customer_surname}"

    def get_email(self, obj):
        user = get_loged_user(obj)
        return user.email

class ClientAccountSerializer(serializers.ModelSerializer):
    account_type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cuenta
        fields = [
            "account_type",
            "balance"
        ]

    def get_account_type(self, obj):
        return obj.cuenta.account_type

class ClientLoansSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prestamo
        fields = [
            "loan_type",
            "loan_total"
        ]

class BranchLoansSerializer(serializers.ModelSerializer):
    branch = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Prestamo
        fields = [
            "branch", 
            "loan_type",
            "loan_total"
        ]

    def get_branch(self, obj):
        return obj.customer_id.branch_id.branch_name
    
class CardsSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)
    brand = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tarjeta
        fields = [
            'owner',
            'card_number',
            'card_grant_date',
            'card_expiration_date',
            'card_type',
            'brand',
        ]
    
    def get_owner(self, obj):
        name = obj.customer.customer_name
        surname = obj.customer.customer_surname
        return f'{name} {surname}'

    def get_brand(self, obj):
        return obj.brand.card_brand

class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = [
            'loan_type',
            'loan_date',
            'loan_total',
        ]

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = [
            'street',
            'number',
            'city',
            'province',
            'country',
        ]


class BranchSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Sucursal
        fields = [
            'branch_name',
            'branch_number',
            'address'
        ]

    def get_address(self, obj):
        return f"{obj.address.street} {str(obj.address.number)}, {obj.address.city}, {obj.address.country}"


