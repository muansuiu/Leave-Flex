from django import forms
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm

from leaveTracker import roles_filename
from leaveTracker.utils.utils import Utils

from .models import Employees, Team

utils = Utils()
TEAM_ROLE_CHOICES = utils.read_json(roles_filename)

class UserRegisterForm(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        empty_label="Select Team"
    )
    
    class Meta:
        model = Employees
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'team', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()

        return user
