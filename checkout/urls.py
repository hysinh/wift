from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/existing/', views.checkout_existing_member, name='checkout_existing_member'),
    path('checkout_success/<purchase_number>', views.checkout_success, name='checkout_success'),
    path('checkout_success/renewal/<purchase_number>', views.checkout_success_renewal, name='checkout_success_renewal'),
]