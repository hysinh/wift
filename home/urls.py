from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # WIFT Public pages
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('fellowships/', views.fellowships, name='fellowships'),
]