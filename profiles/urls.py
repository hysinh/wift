from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/edit_profile/', views.edit_private_data, name='edit_private_data'),
]