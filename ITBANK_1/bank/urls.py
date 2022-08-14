from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='bank-home'),
    path('personal-info/', views.PersonalInfo, name='personal-info'),
    path('security/', views.Security, name='security'),
    path('cards/', views.Cards, name='cards'),
    path('help/', views.Help, name='help'),
    path('expenses/', views.Expenses, name='expenses'),
]
