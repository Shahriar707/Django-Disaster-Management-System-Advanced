from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Donation)
admin.site.register(Crisis)
admin.site.register(Volunteer)
admin.site.register(Inventory)
admin.site.register(Task)