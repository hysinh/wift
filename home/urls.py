from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # django admin panel and all-auth authentication pages
    path('', views.index, name='home'),
]