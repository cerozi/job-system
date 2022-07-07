# django built-in imports;
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse

# other apps imports;
from apps.apply.models import Apply
from apps.authentication.decorators import (only_company_users,
                                            only_employee_users)
from apps.profiles.models import Company, Employee

# current app imports;
from .forms import JobCreateForm
from .models import Job


@login_required
@only_company_users
def job_create(request):
    ''' Creates a job. '''

    form = JobCreateForm(request.POST or None)
    status_code = 200
    if request.method == 'POST':
        if form.is_valid():

            # assigns the company object to the job and saves it;
            company = Company.objects.get(user=request.user)
            form.instance.company = company
            form.save()
            return redirect(reverse('company-home'))
        
        status_code = 422

    return render(request, 'home/job_form.html', {"form": form}, status=status_code)

@login_required
@only_company_users
def job_update(request, pk):
    ''' Updates a job. 
    :param - pk: job object primary key
    '''

    company_obj = Company.objects.get(user=request.user)
    job_qs = Job.objects.filter(pk=pk, company=company_obj)
    status_code = 200

    # checks if the requested job belongs to the request user;
    if not job_qs.exists():
        return redirect(reverse('company-home'))

    job_obj = job_qs[0]
    form = JobCreateForm(request.POST or None, instance=job_obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # updates the job object;
            return redirect(reverse('company-home'))

        status_code = 422

    return render(request, 'home/job_form.html', {"form": form}, status=status_code)

@login_required
@only_company_users
def job_delete(request, pk):
    ''' Deletes a job. 
    :param - pk: job object primary key
    '''

    if request.method == 'POST':
        company_obj = Company.objects.get(user=request.user)
        job_qs = Job.objects.filter(pk=pk, company=company_obj, closed=True)

        # checks if the requested job belongs to the request user;
        if job_qs.exists():
            job_qs[0].delete() # deletes the job object;

    return redirect(reverse('company-jobs'))

@login_required
@only_company_users
def job_close(request, pk):
    ''' Closes a job, so it wont receive applications anymore. 
    :param - pk: job object primary key
    '''

    if request.method == 'POST':
        company_obj = Company.objects.get(user=request.user)
        job_qs = Job.objects.filter(pk=pk, company=company_obj)

        # checks if the requested job belongs to the request user;
        if not job_qs.exists():
            return redirect(reverse('company-home'))

        job_obj = job_qs[0]
        job_obj.closed = True # updates the closed attribute;
        job_obj.save() # saves the job object;

    return redirect(reverse('company-home'))

@login_required
@only_company_users
def job_open(request, pk):
    ''' Opens a job, so it can be able to receive new applications. 
    :param - pk: job object primary key
    '''


    if request.method == 'POST':
        company_obj = Company.objects.get(user=request.user)
        job_qs = Job.objects.filter(pk=pk, company=company_obj, closed=True)

        # checks if the requested job belongs to the request user;
        if not job_qs.exists():
            return redirect(reverse('company-home'))

        job = job_qs[0]
        job.closed = False # updates the closed attribute;
        job.save() # saves job object;

    return redirect(reverse('company-jobs'))

@login_required
@only_company_users
def total_company_jobs(request):
    ''' Get all the company jobs. '''

    from apps.jobs.models import Job
    job_qs = Job.get_company_all_jobs(user=request.user) # queryset with all the jobs that belongs to the request user;

    # pagination
    job_paginator = Paginator(job_qs, 5)
    page = request.GET.get('page')
    jobs = job_paginator.get_page(page)

    return render(request, 'home/company_jobs.html', {"jobs": jobs, "job_paginator": job_paginator})

@login_required
@only_employee_users
def total_jobs(request):
    '''' Get all the jobs. '''

    job_qs = Job.objects.filter(closed=False).order_by('-created') # queryset with all the jobs;
    employee_obj = Employee.objects.get(user=request.user)
    user_applications = Apply.objects.filter(employee=employee_obj)
     # list with all the jobs that te request user applied;
    user_applications_job = [application.job for application in user_applications]

    
    # pagination
    job_paginator = Paginator(job_qs, 5)
    page = request.GET.get('page')
    jobs = job_paginator.get_page(page)

    return render(request, 'home/all_jobs.html', {"jobs": jobs, "user_applications_job":user_applications_job, "job_paginator": job_paginator})

@login_required
def search_job(request):
    ''' Gets all the jobs that contais the search
    :param - job_title: str 
    '''
    
    job_title = request.GET.get('job_title')
    job_qs = Job.objects.filter(title__contains=job_title)
    return render(request, 'home/search_job.html', {"job_title": job_title, "job_qs": job_qs})
