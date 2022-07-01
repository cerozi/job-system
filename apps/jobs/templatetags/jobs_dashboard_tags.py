from django import template
from apps.profiles.models import Company
from apps.jobs.models import Job

register = template.Library()

@register.simple_tag
def get_total_jobs(user):
    company = Company.objects.get(user=user)
    return Job.objects.filter(company=company).count()

@register.simple_tag
def get_total_open_jobs(user):
    company = Company.objects.get(user=user)
    return Job.objects.filter(company=company, closed=False).count()

@register.simple_tag
def get_total_closed_jobs(user):
    company = Company.objects.get(user=user)
    return Job.objects.filter(company=company, closed=True).count()