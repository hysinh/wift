from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/<member_id>', views.dashboard, name='dashboard'),
    path('dashboard/edit_profile/<member_id>', views.edit_private_data, name='edit_private_data'),
    path('dashboard/edit_public_profile/<member_id>', views.edit_public_data, name='edit_public_data'),
]