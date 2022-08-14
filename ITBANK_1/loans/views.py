from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from .forms import LoansForm

# Create your views here.

@login_required
def LoansFormView(request):
    
    form = LoansForm()
    
    context = {
        "form": form
    }
    return render(request, 'loans/loans_form.html', context)