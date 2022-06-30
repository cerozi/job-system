from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.authentication.decorators import only_company_users, only_employee_users

# Create your views here.
@login_required
@only_company_users
def company_home(request):
    print('company access. ')
    return render(request, 'home/index.html', {})

@login_required
@only_employee_users
def employee_home(request):
    print('employee access. ')
    return render(request, 'home/index.html', {})