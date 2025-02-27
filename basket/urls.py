from django.urls import path
from . import views

urlpatterns = [
    path("basket/", views.view_basket, name="view_basket"),
    path("add/<category_id>", views.add_to_basket, name="add_to_basket"),
    path("remove/<category_id>/", views.remove_from_basket, name="remove_from_basket"),
]
