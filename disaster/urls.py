from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # home
    path('', views.home_view, name='home'),
    # authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # donation
    path('donations/', views.donation_list, name='donation_list'),
    path('donations/add/', views.donation_create, name='donation_add'),
    # crisis
    path('crisis/', views.crisis_list, name='crisis_list'),
    path('crisis/add/', views.crisis_create, name='crisis_add'),
    # volunteer
    path('volunteer/', views.volunteer_view, name='volunteer_list'),
    # inventory
    path('inventory/', views.inventory_view, name='inventory_list'),
    # task
    path('task/', views.task_view, name='task_list'),
]