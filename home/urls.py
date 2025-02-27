from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # WIFT Public pages
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('fellowships/', views.fellowships, name='fellowships'),
    path('mentoring/', views.mentoring, name='mentoring'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('join/', views.join, name='join'),
    path('privacy/', views.privacy_policy, name='privacy'),
]