# built-in django imports;
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse

# other apps imports;
from apps.apply.models import Apply
from apps.authentication.decorators import (only_company_users,
                                            only_employee_users)
from apps.jobs.models import Job
from apps.profiles.models import Company, Employee

# current app imports;
from .forms import ApplyForm


@login_required
@only_employee_users
def create_apply(request, pk):
    ''' Creates an application. '''

    form = ApplyForm(request.POST or None)
    job = Job.objects.get(pk=pk)
    employee = Employee.objects.get(user=request.user)
    status_code = 200

    # checks if an application object from the requested employee already exists;
    apply_qs = Apply.objects.filter(job=job, employee=employee)
    if apply_qs.exists():
        return redirect(reverse('employee-home'))

    if request.method == 'POST':
        # checks if the user profile was already filled;
        if not employee.check_null_fields():
            messages.error(request, 'Antes de se candidatar, você precisa preencher seu perfil. ')
            return redirect(reverse('apply', args=(job.pk, )))

        if form.is_valid():

            # assigns the application to the request employee and saves it;
            form.instance.job = job
            form.instance.employee = employee
            form.save()

            return redirect(reverse('employee-home'))
        
        status_code = 422

    return render(request, 'home/apply.html', {"form": form}, status=status_code)

@login_required
@only_employee_users
def update_apply(request, pk):
    ''' Updates application. '''

    employee = Employee.objects.get(user=request.user)
    application_qs = Apply.objects.filter(pk=pk, employee=employee)
    status_code = 200

    # checks if the requested application belongs to the request user;
    if not application_qs.exists():
        return redirect(reverse('employee-home'))

    application = application_qs[0]
    form = ApplyForm(request.POST or None, instance=application)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # updates the application object;
            return redirect(reverse('update-apply', args=(pk, )))
        
        status_code = 422

    return render(request, 'home/apply.html', {"form": form}, status=status_code)

@login_required
@only_employee_users
def delete_apply(request, pk):
    ''' Deletes application. '''

    if request.method == 'POST':
        employee = Employee.objects.get(user=request.user)
        application_qs = Apply.objects.filter(pk=pk, employee=employee)

        # checks if the requested application belongs to the request user;
        if application_qs.exists():
            application = application_qs[0]
            application.delete() # deletes application object;


    return redirect(reverse('employee-home'))

@login_required
@only_employee_users
def get_all_applications(request):
    ''' Get all the applications from the request user. '''

    # queryset for the user applications;
    employee_obj = Employee.objects.get(user=request.user)
    user_applications_qs = Apply.objects.filter(employee=employee_obj, job__closed=False)

    # pagination;
    user_paginator = Paginator(user_applications_qs, 5)
    page = request.GET.get('page')
    user_applications = user_paginator.get_page(page)

    return render(request, 'home/employee_applications.html', {"applications": user_applications, "user_paginator": user_paginator})

@login_required
@only_company_users
def get_job_applications(request, pk):
    ''' Get all the job applications. '''

    company_obj = Company.objects.get(user=request.user)
    job_qs = Job.objects.filter(pk=pk, company=company_obj)

    # checks if the requested job belongs to the request user;
    if not job_qs.exists():
        return redirect(reverse('company-home'))

    job = job_qs[0]
    applications_qs = Apply.objects.filter(job=job)

    # pagination;
    applications_paginator = Paginator(applications_qs, 5)
    page = request.GET.get('page')
    applications = applications_paginator.get_page(page)


    return render(request, 'home/job_applications.html', {"applications": applications, 
                                                        "job": job, 
                                                        'applications_paginator': applications_paginator})
