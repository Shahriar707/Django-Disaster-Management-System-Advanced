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
    path('volunteers/', views.volunteer_list, name='volunteer_list'),
    path('volunteers/add/', views.volunteer_create, name='volunteer_add'),
    # inventory
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/add/', views.inventory_create, name='inventory_add'),
    # task
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.task_create, name='task_add'),
]