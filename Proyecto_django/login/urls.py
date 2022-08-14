from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginRegisterView, name='login-register'),
    path('register-succes/', views.RegisterSucces, name='register-succes'),
    path('activate/<uidb64>/<token>', views.VerificationView.as_view(), name='verification'),
    path('logout/', views.LogoutView, name='logout'),
    path('register-fail/', views.RegisterFail, name='register-fail'),
]
