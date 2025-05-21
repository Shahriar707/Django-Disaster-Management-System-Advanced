from django import forms
from .models import *

class CrisisForm(forms.ModelForm):
    class Meta:
        model = Crisis
        fields = ['title', 'description', 'location', 'severity', 'required_help', 'images']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'required_help': forms.Textarea(attrs={'rows': 3}),
        }


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor_name', 'amount', 'donation_type']
        widgets = {
            'donor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'donation_type': forms.Select(attrs={'class': 'form-select'}),
        }


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['user', 'name', 'age', 'phone_number', 'location', 'assigned_task', 'is_available']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'assigned_task': forms.Select(attrs={'class': 'form-select'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['user'].queryset = User.objects.all()
            self.fields['user'].empty_label = None
            self.fields['assigned_task'].queryset = Task.objects.all()
            self.fields['assigned_task'].empty_label = "No task assigned"


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'quantity', 'inventory_type', 'description', 'added_by', 'crisis']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'inventory_type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'added_by': forms.Select(attrs={'class': 'form-select'}),
            'crisis': forms.Select(attrs={'class': 'form-select'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description']
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }