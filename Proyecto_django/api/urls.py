from django.urls import path
from . import views
  
urlpatterns = [
    path('cliente/', views.ClientDetailAPIView.as_view()),
    path('cuenta/', views.ClientAccountAPIView.as_view()),
    path('prestamo/', views.ClientLoansAPIView.as_view()),
    path('prestamo/sucursal/<int:branch_id>/', views.BranchLoansAPIView.as_view()),
    path('tarjeta/<int:pk>/', views.CardsAPIView.as_view()),
    path('sucursales/', views.BranchAPIView.as_view()),
    path('direccion/modificar/<int:pk>/', views.AddressAPIView.as_view()),
    path('prestamo/crear/<int:pk>/', views.LoanCreateAPIView.as_view()),
    path('prestamo/borrar/<int:pk>/', views.LoanDestroyAPIView.as_view()),
]