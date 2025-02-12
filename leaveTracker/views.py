from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.views.generic.base import TemplateView

from leaveTracker import roles_filename
from leaveTracker.utils.utils import Utils

from .forms import UserRegisterForm
from .models import Team

utils = Utils()
TEAM_ROLE_CHOICES = utils.read_json(roles_filename)

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/sign-up.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Profile Created Successfully"


    def form_valid(self, form):
        user = form.save(commit=False)
        user.team = form.cleaned_data.get("team")  # Ensure team is set
        user.role = form.cleaned_data.get("role")  # Ensure role is set
        user.save()
        return super().form_valid(form)

class EmployeeLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.success(self.request, 'Welcome!')
        return self.success_url
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return super().form_invalid(form)
    
class HomeView(TemplateView):
    template_name = 'home.html'
    
# New API endpoint for fetching roles dynamically
def get_roles(request):
    team_name = request.GET.get("team", "")
    roles = Team.objects.filter(id=team_name).values()[0]['team_name']
    roles = TEAM_ROLE_CHOICES.get(roles, []) # Get roles for selected team
    return JsonResponse({"roles": roles})
