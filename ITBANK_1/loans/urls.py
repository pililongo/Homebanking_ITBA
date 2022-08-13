from django.urls import path
from . import views

urlpatterns = [
    path('', views.Formulario, name='loans-form'),
]
