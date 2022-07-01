from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import JobCreateForm
from apps.profiles.models import Company
from apps.authentication.decorators import only_company_users
from .models import Job

@only_company_users
def job_create(request):
    form = JobCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            company = Company.objects.get(user=request.user)
            form.instance.company = company
            form.save()
            return redirect(reverse('company-home'))

    return render(request, 'home/job_form.html', {"form": form})

@only_company_users
def job_update(request, pk):
    company_obj = Company.objects.get(user=request.user)
    job_qs = Job.objects.filter(pk=pk, company=company_obj)
    if not job_qs.exists():
        return redirect(reverse('company-home'))

    job_obj = job_qs[0]
    form = JobCreateForm(request.POST or None, instance=job_obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('company-home'))

    return render(request, 'home/job_form.html', {"form": form})

@only_company_users
def job_close(request, pk):
    company_obj = Company.objects.get(user=request.user)
    job_qs = Job.objects.filter(pk=pk, company=company_obj)
    if not job_qs.exists():
        return redirect(reverse('company-home'))

    job_obj = job_qs[0]
    if request.method == 'POST':
        job_obj.closed = True
        job_obj.save()

    return redirect(reverse('company-home'))

