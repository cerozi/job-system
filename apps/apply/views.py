from django.shortcuts import render, redirect

from apps.apply.models import Apply
from .forms import ApplyForm
from django.urls import reverse
from apps.jobs.models import Job
from apps.profiles.models import Employee
from apps.authentication.decorators import only_employee_users
from django.contrib.auth.decorators import login_required

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
