# django built-in imports;
from django.shortcuts import redirect, render
from django.urls import reverse

# other apps imports;
from apps.authentication.forms import CustomUserRegisterForm
from apps.profiles.models import Company, Employee

# current app imports;
from .forms import CompanyProfileForm, EmployeeProfileForm


def profile(request):
    ''' Renders request user profile. '''

    if request.user.is_company:
        template_name = 'company_profile'
        company = Company.objects.get(user=request.user)
        form = CompanyProfileForm(request.POST or None, instance=company)
    else:
        template_name = 'user_profile'
        employee = Employee.objects.get(user=request.user)
        form = EmployeeProfileForm(request.POST or None, request.FILES or None, instance=employee)

    status_code = 200
    user_form = CustomUserRegisterForm(request.POST or None, instance=request.user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))

        status_code = 422

    return render(request, f'home/{template_name}.html', {"form": form, "user_form": user_form}, status=status_code)
