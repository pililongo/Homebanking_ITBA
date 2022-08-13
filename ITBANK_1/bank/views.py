from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from clients.models import Cliente
from login.models import Relation

# Create your views here.

@login_required
def Home(request):
    return render(request,'bank/home.html')

@login_required
def PersonalInfo(request):
    user = request.user
    cliente_id = Relation.objects.filter(user_id=user.pk).first().cliente_id
    cliente = Cliente.objects.filter(customer_id= cliente_id).first()

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
    return render(request, 'bank/cards.html')
