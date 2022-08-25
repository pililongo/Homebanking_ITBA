from django.urls import path
from .views import ClientDetailAPIView, ClientAccountAPIView, ClientLoansAPIView, LoansBranchAPIView

urlpatterns = [
    path('cliente/', ClientDetailAPIView.as_view()),
    path('cuenta/', ClientAccountAPIView.as_view()),
    path('prestamo/', ClientLoansAPIView.as_view()),
    path('sucursal-prestamo/<int:pk>', LoansBranchAPIView.as_view()),
]