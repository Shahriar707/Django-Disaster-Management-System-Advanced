from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)

    return redirect('home')


def donation_view(request):
    return render(request, 'donation.html')

def crisis_view(request):
    return render(request, 'crisis.html')

def inventory_view(request):
    return render(request, 'inventory.html')

def volunteer_view(request):
    return render(request, 'volunteer.html')

def task_view(request):
    return render(request, 'task.html')