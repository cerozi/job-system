from django import template
from apps.apply.models import Apply
from apps.profiles.models import Employee, Company

register = template.Library()

@register.simple_tag
def get_employee_applications(user):
    employee_obj = Employee.objects.get(user=user)
    return Apply.objects.filter(employee=employee_obj, job__closed=False).count()


@register.simple_tag
def get_company_applications_count(user):
    company_obj = Company.objects.get(user=user)
    return Apply.objects.filter(job__company=company_obj, job__closed=False).count()

@register.simple_tag
def get_job_applications_count(job):
    return Apply.objects.filter(job=job, job__closed=False).count()


@register.simple_tag
def get_employee_points(application):
    points = 0

    if int(application.job.scholarship) <= int(application.employee.scholarship):
        points += 1

    if application.job.salary == application.salary:
        points += 1

    return points