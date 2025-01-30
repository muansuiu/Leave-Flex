from django.contrib import admin
from .models import Employees, Team, LeaveRequest

# Register your models here.

admin.site.register(Employees)
admin.site.register(Team)
admin.site.register(LeaveRequest)