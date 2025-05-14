from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('donations/', views.donation_view, name='donation_list'),
    path('crisis/', views.crisis_view, name='crisis_list'),
    path('volunteer/', views.volunteer_view, name='volunteer_list'),
    path('inventory/', views.inventory_view, name='inventory_list'),
    path('task/', views.task_view, name='task_list'),
]