from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.view_basket, name='view_basket'),
    path('basket/test', views.view_basket_test, name='view_basket_test'),
    path('add/<category_id>', views.add_to_basket_test, name='add_to_basket_test')
]