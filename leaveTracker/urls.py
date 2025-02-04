from django.urls import path

from .views import EmployeeLoginView, SignUpView, get_roles

urlpatterns = [
    path('sign-up', SignUpView.as_view(), name='sign-up'),
    path('login/', EmployeeLoginView.as_view(), name='login'),
    path('get_roles/', get_roles, name='get_roles'),
]
