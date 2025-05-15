from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import CrisisForm, DonationForm

# Create your views here.

@login_required(login_url='/login/')
def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST.get('username')
        duplicate = False
        if username and User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            duplicate = True

        if not duplicate and form.is_valid():
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

    return redirect('login')


def donation_list(request):
    donations = Donation.objects.order_by('-date')
    total_amount = Donation.objects.aggregate(models.Sum('amount'))['amount__sum'] or 0

    return render(request, 'donation.html', {'donations': donations, 'total_amount': total_amount})


def donation_create(request):
    form = DonationForm()
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm()

    return render(request, 'donation_form.html', {'form': form})


def crisis_list(request):
    all_crisis = Crisis.objects.filter(is_approved=True, status='open').order_by('-date_reported')

    return render(request, 'crisis.html', {'all_crisis': all_crisis})


def crisis_create(request):
    form = CrisisForm(request.POST)
    if request.method == 'POST':
        form = CrisisForm(request.POST)
        if form.is_valid():
            crisis = form.save(commit=False)
            if request.user.is_authenticated:
                crisis.added_by = request.user
            crisis.save()
            return redirect('crisis_list')
    else:
        form = CrisisForm()

    return render(request, 'crisis_form.html', {'form': form})


def inventory_view(request):
    return render(request, 'inventory.html')

def volunteer_view(request):
    return render(request, 'volunteer.html')

def task_view(request):
    return render(request, 'task.html')