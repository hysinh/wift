from django.urls import path
from . import views

urlpatterns = [
    # path('checkout/', views.checkout, name='checkout'),
    path('checkout/test/', views.checkout_test, name='checkout_test'),
    path('checkout_success/<purchase_number>', views.checkout_success, name='checkout_success'),
]