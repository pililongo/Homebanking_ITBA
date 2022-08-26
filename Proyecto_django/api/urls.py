from django.urls import path
from .views import ClientDetailAPIView, ClientAccountAPIView, ClientLoansAPIView, BranchLoansAPIView

urlpatterns = [
    path('cliente/', ClientDetailAPIView.as_view()),
    path('cuenta/', ClientAccountAPIView.as_view()),
    path('prestamo/', ClientLoansAPIView.as_view()),
    path('sucursal-prestamo/<int:branch_id>/', BranchLoansAPIView.as_view()),
]