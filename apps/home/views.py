# django built-in imports;
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# other apps imports;
from apps.apply.models import Apply
from apps.authentication.decorators import (only_company_users,
                                            only_employee_users)
from apps.jobs.models import Job


@login_required
@only_company_users
def company_home(request):
    ''' Company user home. '''

    jobs = Job.get_company_active_jobs(user=request.user)[:4]

    return render(request, 'home/company_home.html', {"jobs": jobs})

@login_required
@only_employee_users
def employee_home(request):
    ''' Employee user home. '''

    applications = Apply.get_all_employee_applications(user=request.user)[:5]
    jobs = Job.objects.filter(closed=False).order_by('-created')[:5]
    return render(request, 'home/employee_home.html', {"applications": applications, "jobs": jobs})
