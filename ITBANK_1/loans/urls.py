from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoansFormView, name='loans-form'),
]
