from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.core.mail import EmailMessage
from homebanking import settings
from django.contrib.auth.models import User
from .utils import TokenGenerator
from .models import Relation
from clients.models import Cliente
from django.views import View
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.

def LoginRegisterView(request):
    if request.method == 'POST' and request.POST.get('form-type') == 'r_form':
        r_form = UserRegisterForm(request.POST)
        if r_form.is_valid():
            if len(Cliente.objects.filter(customer_dni=r_form.cleaned_data['dni'])) == 1:
                
                r_form.save()
                
                user = User.objects.filter(username=r_form.cleaned_data['username']).first()
                cliente = Cliente.objects.filter(customer_dni=r_form.cleaned_data['dni']).first()
                
                relation = Relation(user= user, cliente = cliente)
                
                relation.save()
                
                user.is_active = False
                user.save()

                domain = get_current_site(request).domain

                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = TokenGenerator.make_token(user)
    
                link = 'http://'+ domain + '/activate/'+ str(uidb64) + '/' + str(token) 

                email = EmailMessage(
                    f'Te damos la bienvenida {user} a ITBANK!',
                    f'Para completar tu registro por favor ingresá al siguiente link: '+ link + '\n\nSaludos cordiales. \n\nEquipo de ITBANK.',
                    settings.EMAIL_HOST_USER,
                    (user.email,),
                )
                email.send()

                return redirect('register-succes')
            else:
                return redirect('register-fail')
    else:
        r_form = UserRegisterForm()

    if request.method == 'POST' and request.POST.get('form-type') == 'l_form':
        l_form = AuthenticationForm(request, data=request.POST)
        user = User.objects.filter(username = request.POST.get('username')).first()
        if l_form.is_valid():
            login(request, user)
            return redirect('bank-home')
    else:
        l_form = AuthenticationForm(request)

    context = {
        "r_form" : r_form,
        "l_form" : l_form,      
    }
    
    return render(request, 'login/login_register.html', context)


def RegisterSucces(request):
    context = {
        "title" : "¡Tu registro ha sido exitoso!",
        "description" : "Por favor, verificá tu correo y seguí las instrucciones para activar tu cuenta.",
        "link_message" : "Volver al inicio",
    }
    return render(request, 'login/base_message.html',context)

def RegisterFail(request):
    context = {
        "title" : "No pudimos verificarte como cliente",
        "description" : "Por favor acercate a una sucursal para crearte una cuenta en ITBANK",
        "link_message" : "Vuelve al inicio",
    }
    return render(request, 'login/base_message.html',context)

class VerificationView(View):
    def get(self, request, uidb64, token):
        
        id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.filter(pk=id).first()

        if not TokenGenerator.check_token(user,token):
            context = {
                "title" : "Tu cuenta ya se encuentra activa",
                "description" : " ",
                "link_message" : "Ingresa aquí"
            }
            return render(request, 'login/base_message.html', context)
            
        if user.is_active:
            context = {
                "title" : "Tu cuenta ya se encuentra activa",
                "description" : " ",
                "link_message" : "Ingresa aquí"
            }
            return render(request, 'login/base_message.html', context)
        else:
            user.is_active = True
            user.save()
            
            context = {
                "title" : "Tu cuenta ha sido activada",
                "description" : "Ahora puedes operar en ITBANK ingresando a tu cuenta",
                "link_message" : "Ingresar aquí"
            }
            return render(request, 'login/base_message.html', context)


def LogoutView(request):
    logout(request)
    context = {
        "title" : "Tu sesión ha sido cerrada con éxito",
        "description" : "Para volver a operar en ITBANK debes iniciar sesión",
        "link_message" : "Ingresar aquí"
    }
    return render(request, 'login/base_message.html', context)