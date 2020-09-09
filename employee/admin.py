from django.contrib import admin
from .models import Employee,leave_application
# Register your models here.
admin.site.register(Employee)
admin.site.register(leave_application)