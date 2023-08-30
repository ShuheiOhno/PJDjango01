from django.contrib import admin
from .models import Store, Staff, Booking

# Register your models here.
admin.site.register(Store)
admin.site.register(Staff)
admin.site.register(Booking)