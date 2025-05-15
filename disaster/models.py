from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donation(models.Model):
    donor_name = models.CharField(max_length=120)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField(auto_now_add=True)
    donation_type = models.CharField(max_length=50, choices=[('one_time', 'One Time'), ('recurring', 'Recurring')], default='one_time')

    def __str__(self):
        return f'{self.donor_name} - {self.amount}'


class Crisis(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('pending', 'Pending')
    ]
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]
    title = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    date_reported = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    required_help = models.TextField(max_length=500, default='Not specified')
    images = models.ImageField(upload_to='crisis_photos/', null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    assigned_task = models.ForeignKey('Task', on_delete=models.SET_NULL, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Inventory(models.Model):
    INVENTORY_TYPES = [
        ('Relief', 'Relief'),
        ('Expenses', 'Expenses')
    ]
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    inventory_type = models.CharField(max_length=100, choices=INVENTORY_TYPES)
    description = models.CharField(max_length=1000, null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    crisis = models.ForeignKey(Crisis, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.item_name}'


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.task_name}'