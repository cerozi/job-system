from django.shortcuts import render, redirect

from apps.apply.models import Apply
from .forms import ApplyForm
from django.urls import reverse
from apps.jobs.models import Job
from apps.profiles.models import Company, Employee
from apps.authentication.decorators import only_company_users, only_employee_users
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

@login_required
@only_employee_users
def create_apply(request, pk):
    form = ApplyForm(request.POST or None)
    job = Job.objects.get(pk=pk)
    employee = Employee.objects.get(user=request.user)

    apply_qs = Apply.objects.filter(job=job, employee=employee)
    if apply_qs.exists():
        return redirect(reverse('employee-home'))

    if request.method == 'POST':
        if form.is_valid():

            form.instance.job = job
            form.instance.employee = employee
            form.save()

            return redirect(reverse('employee-home'))

    return render(request, 'home/apply.html', {"form": form})

@login_required
@only_employee_users
def update_apply(request, pk):
    employee = Employee.objects.get(user=request.user)
    application_qs = Apply.objects.filter(pk=pk, employee=employee)
    if not application_qs.exists():
        return redirect(reverse('employee-home'))

    application = application_qs[0]
    form = ApplyForm(request.POST or None, instance=application)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('update-apply', args=(pk, )))

    return render(request, 'home/apply.html', {"form": form})

@login_required
@only_employee_users
def delete_apply(request, pk):
    if request.method == 'POST':
        employee = Employee.objects.get(user=request.user)
        application_qs = Apply.objects.filter(pk=pk, employee=employee)
        if application_qs.exists():
            application = application_qs[0]
            application.delete()


    return redirect(reverse('employee-home'))

@login_required
@only_employee_users
def get_all_applications(request):
    employee_obj = Employee.objects.get(user=request.user)
    user_applications_qs = Apply.objects.filter(employee=employee_obj, job__closed=False)

    user_paginator = Paginator(user_applications_qs, 5)
    page = request.GET.get('page')
    user_applications = user_paginator.get_page(page)

    return render(request, 'home/employee_applications.html', {"applications": user_applications, "user_paginator": user_paginator})

@login_required
@only_company_users
def get_job_applications(request, pk):
    company_obj = Company.objects.get(user=request.user)
    job_qs = Job.objects.filter(pk=pk, company=company_obj)
    if not job_qs.exists():
        return redirect(reverse('company-home'))

    job = job_qs[0]
    applications = Apply.objects.filter(job=job)
    return render(request, 'home/job_applications.html', {"applications": applications, "job": job})