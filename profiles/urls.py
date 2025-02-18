from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/<member_id>', views.dashboard, name='dashboard'),
    path('dashboard/edit_profile/<member_id>', views.edit_private_data, name='edit_private_data'),
]