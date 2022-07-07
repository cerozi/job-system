# django built-in imports;
from django.urls import path

# current app imports;
from .views import employee_home, company_home

urlpatterns = [
    path('', employee_home, name='employee-home'),
    path('dashboard/', company_home, name='company-home')
]