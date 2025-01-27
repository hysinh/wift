from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.view_basket, name='view_basket'),
]