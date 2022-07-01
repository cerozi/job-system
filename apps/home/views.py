from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.authentication.decorators import only_company_users, only_employee_users

@login_required
@only_company_users
def company_home(request):
    from apps.jobs.models import Job
    jobs = Job.get_company_active_jobs(user=request.user)[:5]

    return render(request, 'home/index.html', {"jobs": jobs})

@login_required
@only_employee_users
def employee_home(request):
    print('employee access. ')
    return render(request, 'home/index.html', {})