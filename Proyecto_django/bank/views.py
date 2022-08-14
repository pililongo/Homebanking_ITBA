from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from clients.models import Cliente
from login.models import Relation
from accounts.models import Cuenta
from cards.models import Tarjeta

# Create your views here.

@login_required
def Home(request):
    cliente = get_loged_client(request)
    
    client_type = cliente.client.client_type

    sucursal = cliente.branch_id
    branch_name = sucursal.branch_name

    accounts = Cuenta.objects.filter(customer_id = cliente.pk)

    context = {
        "client_type" : client_type,
        "branch_name" : branch_name,
        "accounts" : accounts,
    }

    return render(request,'bank/home.html', context)

@login_required
def PersonalInfo(request):
    cliente = get_loged_client(request)

    dob = cliente.dob
    dni = cliente.customer_dni

    address = cliente.address_id.street + ' ' + str(cliente.address_id.number)+ ', ' + cliente.address_id.city + ', ' + cliente.address_id.country

    context = {
        "dob" : dob,
        "dni" : dni,
        "address" : address,
    }

    return render(request, 'bank/personal_info.html', context)

@login_required
def Security(request):
    return render(request, 'bank/security.html')


@login_required
def Cards(request):
    
    cliente = get_loged_client(request)
    cards = Tarjeta.objects.filter(customer = cliente)
    context = {
        "cards" : cards,
    }
    return render(request, 'bank/cards.html', context)


@login_required
def Help(request):
    return render(request, 'bank/ayuda.html')

@login_required
def Expenses(request):
    return render(request, 'bank/app_gastos.html')

def get_loged_client(request):
    user = request.user
    cliente_id = Relation.objects.filter(user_id=user.pk).first().cliente_id
    return Cliente.objects.filter(customer_id= cliente_id).first()