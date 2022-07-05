from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import JobCreateForm
from apps.profiles.models import Company, Employee
from apps.authentication.decorators import only_company_users, only_employee_users
from .models import Job
from django.contrib.auth.decorators import login_required
from apps.apply.models import Apply
from django.core.paginator import Paginator

@login_required
@only_company_users
def job_create(request):
    form = JobCreateForm(request.POST or None)
    status_code = 200
    if request.method == 'POST':
        if form.is_valid():
            company = Company.objects.get(user=request.user)
            form.instance.company = company
            form.save()
            return redirect(reverse('company-home'))
        
        status_code = 422

    return render(request, 'home/job_form.html', {"form": form}, status=status_code)

@login_required
@only_company_users
def job_update(request, pk):
    company_obj = Company.objects.get(user=request.user)
    job_qs = Job.objects.filter(pk=pk, company=company_obj)
    status_code = 200

    if not job_qs.exists():
        return redirect(reverse('company-home'))

    job_obj = job_qs[0]
    form = JobCreateForm(request.POST or None, instance=job_obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('company-home'))

        print(form.errors)
        status_code = 422

    return render(request, 'home/job_form.html', {"form": form}, status=status_code)

@login_required
@only_company_users
def job_delete(request, pk):
    if request.method == 'POST':
        company_obj = Company.objects.get(user=request.user)
        job_qs = Job.objects.filter(pk=pk, company=company_obj, closed=True)
        if job_qs.exists():
            job_qs[0].delete()

    return redirect(reverse('company-jobs'))

@login_required
@only_company_users
def job_close(request, pk):
    if request.method == 'POST':
        company_obj = Company.objects.get(user=request.user)
        job_qs = Job.objects.filter(pk=pk, company=company_obj)
        if not job_qs.exists():
            return redirect(reverse('company-home'))

        job_obj = job_qs[0]
        job_obj.closed = True
        job_obj.save()

    return redirect(reverse('company-home'))

@login_required
@only_company_users
def job_open(request, pk):
    if request.method == 'POST':
        company_obj = Company.objects.get(user=request.user)
        job_qs = Job.objects.filter(pk=pk, company=company_obj, closed=True)
        if not job_qs.exists():
            return redirect(reverse('company-home'))

        job = job_qs[0]
        job.closed = False
        job.save()

    return redirect(reverse('company-jobs'))

@login_required
@only_company_users
def total_company_jobs(request):
    from apps.jobs.models import Job
    job_qs = Job.get_company_all_jobs(user=request.user)

    job_paginator = Paginator(job_qs, 5)
    page = request.GET.get('page')
    jobs = job_paginator.get_page(page)

    return render(request, 'home/company_jobs.html', {"jobs": jobs, "job_paginator": job_paginator})

@login_required
@only_employee_users
def total_jobs(request):
    job_qs = Job.objects.filter(closed=False).order_by('-created')
    employee_obj = Employee.objects.get(user=request.user)
    user_applications = Apply.objects.filter(employee=employee_obj)
    user_applications_job = [application.job for application in user_applications]

    job_paginator = Paginator(job_qs, 5)
    page = request.GET.get('page')
    jobs = job_paginator.get_page(page)

    return render(request, 'home/all_jobs.html', {"jobs": jobs, "user_applications_job":user_applications_job, "job_paginator": job_paginator})

@login_required
def search_job(request):
    job_title = request.GET.get('job_title')
    job_qs = Job.objects.filter(title__contains=job_title)
    return render(request, 'home/search_job.html', {"job_title": job_title, "job_qs": job_qs})
