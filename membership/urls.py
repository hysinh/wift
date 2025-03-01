from . import views
from django.urls import path


urlpatterns = [
    path('join/', views.all_categories, name='join')
]
