from django.db import models
from django.contrib.auth.models import AbstractUser
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