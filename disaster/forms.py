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