from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .utils.utils import Utils

# Create your models here.
class Employees(AbstractUser):

    role = models.CharField(max_length=50,blank=False)
    team = models.ForeignKey(
        'Team', 
        on_delete=models.CASCADE, 
        related_name='team',
        blank=True,
        null=True
    )

    leave_balance = models.IntegerField(default=Utils.calculate_leave_balance)

    def __str__(self):
        return self.username
    
class Team(models.Model):
    team_name = models.CharField(max_length=50,blank=False)
    team_lead = models.OneToOneField(
        'Employees', 
        on_delete=models.SET_NULL, 
        related_name='team_lead',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.team_name

class LeaveRequest(models.Model):
    leave_type_choices = [
        ('sick_leave', 'Sick Leave'),
        ('casual_leave', 'Casual Leave'),
    ]
    employee = models.ForeignKey(
        'Employees', 
        on_delete=models.CASCADE, 
        related_name='employee',
        blank=False,
        null=False
    )
    leave_type = models.CharField(
        max_length=20,
        choices=leave_type_choices,
        default='chose one',
        blank=False
    )
    leave_start_date = models.DateField(blank=False)
    leave_end_date = models.DateField(blank=False)
    leave_reason = models.TextField(max_length=250, blank=False)
    leave_applied_date = models.DateField(default=timezone.now, blank=False)
    leave_status = models.CharField(max_length=50,blank=False)
    lead_approval = models.ForeignKey(
        'Employees',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lead_approval'
    )
    hr_approval = models.ForeignKey(
        'Employees',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='hr_approval'
    )
    leave_approval_date = models.DateField(blank=True, null=True)
    rejected_by = models.ForeignKey(
        'Employees',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    rejection_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return f"{self.employee} {self.leave_type}"
    class Meta:
        verbose_name_plural = 'Leave Requests'
        ordering = ['leave_applied_date']