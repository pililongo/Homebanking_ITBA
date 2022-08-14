import imp
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoansForm
from .models import Prestamo
from accounts.models import Cuenta
from bank.views import get_loged_client
# Create your views here.

@login_required
def LoansFormView(request):
    if request.method == 'POST':
        form = LoansForm(request.POST)
        cliente = get_loged_client(request)
        accounts = Cuenta.objects.filter(customer_id = cliente.pk)

        if have_caja_de_ahorro(accounts):
            client_type = cliente.client.client_type
            PAA = {
                "Classic" : 100_000,
                "Gold" : 300_000,
                "Black" : 500_000,
            }
            print(PAA[client_type])
            print(int(request.POST.get('loan_total')))

            if PAA[client_type] >= int(request.POST.get('loan_total')):
                id = len(Prestamo.objects.all()) + 1
                loan = Prestamo(id,request.POST.get('loan_type'),request.POST.get('loan_date'),request.POST.get('loan_total'), cliente.pk)
                loan.save()
                account = get_caja_de_ahorro(accounts)
                account.balance += int(request.POST.get('loan_total'))
                account.save()

                context = {
                    "title" : "Tu préstamo ha sido aprobado",
                    "description" : "Revisa tu balance",
                    "link_message" : "Volver",
                }
                return render(request, 'loans/base_message_loans.html', context)
            else:
                context = {
                    "title" : "Solicitud de préstamo denegada",
                    "description" : "Ha superado su limite máximo de solicitud",
                    "link_message" : "Volver",
                }
                return render(request, 'loans/base_message_loans.html', context)
        else:
            context = {
                "title" : "Solicitud de préstamo denegada",
                "description" : "No posee caja de ahorro en pesos",
                "link_message" : "Volver",
            }
            return render(request, 'loans/base_message_loans.html', context)
    else:
        form = LoansForm()

    context = {
        "form": form
    }

    return render(request, 'loans/loans_form.html', context)


def have_caja_de_ahorro(accounts):
    for account in accounts:
        if account.cuenta.account_type == 'Caja ahorro pesos':
            return True
    return False

def get_caja_de_ahorro(accounts):
    for account in accounts:
        if account.cuenta.account_type == 'Caja ahorro pesos':
            return account
    return None
