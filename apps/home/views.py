from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.authentication.decorators import only_company_users, only_employee_users
from apps.jobs.models import Job
from apps.apply.models import Apply

@login_required
@only_company_users
def company_home(request):
    jobs = Job.get_company_active_jobs(user=request.user)[:5]

    return render(request, 'home/company_home.html', {"jobs": jobs})

@login_required
@only_employee_users
def employee_home(request):
    applications = Apply.get_all_employee_applications(user=request.user)[:5]
    jobs = Job.objects.all().order_by('-created')[:5]
    return render(request, 'home/employee_home.html', {"applications": applications, "jobs": jobs})