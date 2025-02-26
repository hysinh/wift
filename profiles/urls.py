from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/<member_id>', views.dashboard, name='dashboard'),
    path('dashboard/edit_profile/<member_id>', views.edit_private_data, name='edit_private_data'),
    path('dashboard/edit_public_profile/<member_id>', views.edit_public_data, name='edit_public_data'),
    path('dashboard/create_public_profile/<member_id>', views.create_public_data, name='create_public_data'),
    path('dashboard/purchase_receipts/<member_id>', views.membership_purchases, name='membership_purchases'),
    path('dashboard/member_directory/<member_id>', views.member_directory, name='member_directory'),
    path('delete-profile/<member_id>/', views.delete_public_data, name='delete_public_data'),
]