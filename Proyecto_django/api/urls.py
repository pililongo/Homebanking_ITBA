from django.urls import path
from .views import (
    ClientDetailAPIView, 
    ClientAccountAPIView, 
    ClientLoansAPIView,
    BranchLoansAPIView,
    CardsAPIView,
    BranchAPIView,
    AddressAPIView,
    LoanCreateAPIView,
    LoanDestroyAPIView)

urlpatterns = [
    path('cliente/', ClientDetailAPIView.as_view()),
    path('cuenta/', ClientAccountAPIView.as_view()),
    path('prestamo/', ClientLoansAPIView.as_view()),
    path('sucursal-prestamo/<int:branch_id>/', BranchLoansAPIView.as_view()),
    path('tarjeta/<int:pk>/', CardsAPIView.as_view()),
    path('sucursales/', BranchAPIView.as_view()),
    path('modificar-direccion/<int:pk>/', AddressAPIView.as_view()),
    path('crear-prestamo/<int:pk>/', LoanCreateAPIView.as_view()),
    path('borrar-prestamo/<int:pk>/', LoanDestroyAPIView.as_view()),
]